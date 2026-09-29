"""Conservative evidence check for an official HTML author block without affiliations."""
from html.parser import HTMLParser
import re


class AuthorBlock(HTMLParser):
    def __init__(self):
        super().__init__()
        self.depth = 0
        self.names = 0
        self.complete = False
        self.text = []
        self.name_depth = 0
        self.has_affiliation = False

    def handle_starttag(self, tag, attrs):
        classes = dict(attrs).get("class", "").split()
        if "ltx_authors" in classes:
            self.depth = 1
            return
        if self.depth:
            if tag not in {"br", "hr", "img", "input", "meta", "link", "wbr"}:
                self.depth += 1
            if "ltx_personname" in classes:
                self.names += 1
                self.name_depth = self.depth
            if any("affiliation" in c or "address" in c for c in classes):
                self.has_affiliation = True

    def handle_endtag(self, tag):
        if self.depth:
            if self.depth == self.name_depth:
                self.name_depth = 0
            self.depth -= 1
            if not self.depth:
                self.complete = True

    def handle_data(self, data):
        if self.depth and not self.name_depth:
            self.text.append(data)


def author_block_has_no_affiliation(html: str) -> bool:
    parser = AuthorBlock()
    parser.feed(html)
    if not parser.complete or not parser.names or parser.has_affiliation:
        return False
    residual = " ".join(parser.text)
    residual = re.sub(r"[\w.+-]+\s*(?:@|\bat\b)\s*[\w.-]+\.[a-zA-Z]{2,}", "", residual)
    residual = re.sub(r"\b(?:thanks|e-mail|email)\s*:", "", residual, flags=re.I)
    return not re.search(r"\w", residual)
