// Run with: node --test tests/report-loading.test.cjs
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const root = path.resolve(__dirname, '..');
const source = fs.readFileSync(path.join(root, 'docs/index.html'), 'utf8')
  .match(/<script>([\s\S]*?)<\/script>/)[1]
  .replace('      loadRepoStars();', '').replace('      loadReports();', '');

function setup(fetch, search = '') {
  const nodes = new Map();
  const node = () => ({ innerHTML: '', textContent: '', attrs: {}, children: [],
    addEventListener(type, callback) { this[type] = callback; },
    querySelector: () => node(), querySelectorAll: () => [],
    setAttribute(key, value) { this.attrs[key] = value; },
    append(...children) { this.children.push(...children); },
    classList: { contains: () => false, toggle() {} },
  });
  const storage = new Map();
  const context = vm.createContext({ console, URL, URLSearchParams, AbortController,
    setTimeout, clearTimeout, fetch,
    document: { getElementById(id) { if (!nodes.has(id)) nodes.set(id, node()); return nodes.get(id); },
      createElement: node, querySelector: node, addEventListener() {} },
    window: { location: { protocol: 'http:', search, hash: '', href: `http://localhost/docs/${search}` }, addEventListener() {} },
    history: { state: { paperOverlay: false }, replaceState() {}, pushState() {} },
    localStorage: { getItem: key => storage.get(key) || null, setItem: (key, value) => storage.set(key, value) },
  });
  vm.runInContext(source, context);
  return { context, nodes, run: code => vm.runInContext(code, context) };
}
const ok = text => ({ ok: true, text: async () => text });
const markdown = date => `# 日报 ${date}\n\n## 📌 今日概况\n\n测试日报。\n`;

test('paper detail preserves metadata and TLDR with one abstract and navigable analysis', () => {
  const app = setup();
  const issue = { number: 1, title: '[20260928] Example paper', labels: [], body:
    '## 📋 基础信息\n\n| 字段 | 内容 |\n| --- | --- |\n| 作者 | Alice, Bob |\n| 单位 | Example University |\n| 摘要 | Unique abstract text |\n| TL;DR | Key finding |\n\n## ❓ 10 问题深度分析\n\n### Q1: Problem\nA useful analysis.\n' };
  app.run(`renderIssueDetail(${JSON.stringify(issue)})`);
  const html = app.nodes.get('paperDetail').innerHTML;
  assert.match(html, /Alice, Bob/);
  assert.match(html, /Example University/);
  assert.match(html, /Key finding/);
  assert.equal(html.split('Unique abstract text').length - 1, 1);
  assert.match(html, /id="analysis-0"/);
  assert.match(app.nodes.get('detailNav').innerHTML, /data-section="detail-analysis"/);
});

test('first paint requests only the index and selected report; older deep links work', async () => {
  for (const search of ['', '?date=20260305']) {
    const calls = [];
    const dates = ['20260928', '20260927', '20260305'];
    const app = setup(async url => {
      calls.push(url);
      return ok(url.endsWith('.json') ? JSON.stringify({ dates }) : markdown(url.match(/(\d{8})\.md/)[1]));
    }, search);
    await app.run('loadReports()');
    assert.equal(calls.length, 2);
    assert.equal(calls[0], './daily_reports/index.json');
    assert.match(calls[1], search ? /20260305.md$/ : /20260928.md$/);
    assert.match(app.nodes.get('reportDetail').innerHTML, search ? /2026-03-05/ : /2026-09-28/);
  }
});

test('late completion never replaces a newer selected date', async () => {
  let finishOld;
  const app = setup(url => url.includes('20260927')
    ? new Promise(resolve => { finishOld = () => resolve(ok(markdown('20260927'))); })
    : Promise.resolve(ok(markdown('20260928'))));
  app.run('allReports = [{date:"20260928"}, {date:"20260927"}];');
  const old = app.run('selectReport("20260927")');
  await app.run('selectReport("20260928")');
  finishOld();
  await old;
  assert.match(app.nodes.get('reportDetail').innerHTML, /2026-09-28/);
  assert.equal(app.run('currentReportDate'), '20260928');
});

test('failure shows retry and permits recovery', async () => {
  let fail = true;
  const app = setup(async () => fail ? { ok: false, status: 503 } : ok(markdown('20260928')));
  app.run('allReports = [{date:"20260928"}];');
  await app.run('selectReport("20260928")');
  assert.match(app.nodes.get('loadSummary').textContent, /503/);
  const retry = app.nodes.get('loadSummary').children.at(-1);
  assert.equal(retry.textContent, '重试此日报');
  fail = false;
  await retry.click();
  assert.match(app.nodes.get('reportDetail').innerHTML, /2026-09-28/);
});

test('timeout aborts stalled requests including response bodies', async () => {
  const app = setup(async (url, { signal }) => ({ ok: true, text: () => new Promise((resolve, reject) => {
    signal.addEventListener('abort', () => reject(Object.assign(new Error(), { name: 'AbortError' })));
  }) }));
  app.context.setTimeout = callback => setTimeout(callback, 5);
  await assert.rejects(app.run('fetchText("/slow")'), /请求超时/);
});

test('offline refresh preserves last report and uses cached index', async () => {
  const app = setup(async () => { throw new Error('offline'); });
  app.run(`saveCache("report-dates", ["20260928"]); saveCache("last-report", ${JSON.stringify({date:'20260928', markdown:markdown('20260928')})});`);
  await app.run('loadReports()');
  assert.match(app.nodes.get('reportDetail').innerHTML, /2026-09-28/);
  assert.match(app.nodes.get('loadSummary').textContent, /缓存/);
});

test('direct file opening explains the required local server', async () => {
  const app = setup(() => { throw new Error('must not fetch'); });
  app.run('window.location.protocol = "file:";');
  await app.run('loadReports()');
  assert.match(app.nodes.get('reportDetail').innerHTML, /http.server/);
});

test('all published reports match the archive and pass the parser', async () => {
  const app = setup(async url => ok(fs.readFileSync(path.join(root, 'docs', url), 'utf8')));
  const dates = JSON.parse(fs.readFileSync(path.join(root, 'docs/daily_reports/index.json'))).dates;
  assert.ok(dates.length > 0);
  for (const date of dates) {
    const relative = `daily_reports/${date.slice(0, 6)}/${date}.md`;
    assert.deepEqual(fs.readFileSync(path.join(root, relative)), fs.readFileSync(path.join(root, 'docs', relative)));
    assert.equal((await app.run(`fetchReport("./daily_reports", "${date}")`)).date, date);
  }
});
