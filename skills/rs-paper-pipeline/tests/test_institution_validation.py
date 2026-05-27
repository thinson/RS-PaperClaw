from pathlib import Path
import sys
import tarfile
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from services.digest_builder import build_digest_with_llm, is_invalid_digest_institution
from services.paper_analysis import (
    extract_institutions_from_first_page,
    extract_institutions_from_latex_source,
    is_valid_institution_text,
)


class InstitutionValidationTest(unittest.TestCase):
    def test_rejects_body_text_bleed_in_institution(self):
        value = (
            "Shen Yuan Honors College, Beihang University；"
            "the College of Computing and patches. While this processing strategy can capture abun-"
        )

        self.assertFalse(is_valid_institution_text(value))
        self.assertTrue(is_invalid_digest_institution(value))

    def test_accepts_common_affiliation_list(self):
        value = (
            "Faculty of Applied Sciences, Macao Polytechnic University；"
            "Pazhou Lab (Huangpu)；Macao Polytechnic University"
        )

        self.assertTrue(is_valid_institution_text(value))
        self.assertFalse(is_invalid_digest_institution(value))

    def test_builds_empty_digest_from_stats(self):
        digest = build_digest_with_llm(
            "20260524",
            [],
            stats={"candidate_count": 0, "llm_selected_count": 0},
        )

        self.assertIn("# 日报 20260524", digest)
        self.assertIn("最终纳入日报 0 篇", digest)
        self.assertIn("当日未检索到符合条件并纳入日报的论文", digest)

    def test_extracts_icml_affiliations_from_source(self):
        tex = r"""
        \begin{icmlauthorlist}
          \icmlauthor{Chenyou Guo}{equal,ouc}
        \end{icmlauthorlist}
        \icmlaffiliation{ouc}{Ocean University of China}
        \icmlaffiliation{pku}{Peking University}
        \icmlaffiliation{monash}{Monash University}
        """
        with tempfile.TemporaryDirectory() as temp_dir:
            source_path = Path(temp_dir) / "source.tar"
            tex_path = Path(temp_dir) / "example_paper.tex"
            tex_path.write_text(tex, encoding="utf-8")
            with tarfile.open(source_path, "w") as archive:
                archive.add(tex_path, arcname="example_paper.tex")

            institutions = extract_institutions_from_latex_source(source_path)

        self.assertEqual(
            institutions,
            "Ocean University of China；Peking University；Monash University",
        )

    def test_extracts_footnote_affiliations_before_email(self):
        first_page = """
        Geo-Expert: Towards Expert-Level Geological Reasoning
        Chenyou Guo * 1 Zongqi Liu * 1 Yizhou Zhang * 1 Zhaorui Jiang * 2 3 Ze Liu 1
        Abstract
        While general-purpose Large Language Models applied to Geology often hallucinate.
        1 Ocean University of China 2 Peking University 3 Monash University. Correspondence to: Zhaorui Jiang <zrjiang25@stu.pku.edu.cn>, Ze Liu <liuze@ouc.edu.cn>.
        """

        institutions = extract_institutions_from_first_page("Geo-Expert", "Chenyou Guo", first_page)

        self.assertEqual(
            institutions,
            "Ocean University of China；Peking University；Monash University",
        )


if __name__ == "__main__":
    unittest.main()
