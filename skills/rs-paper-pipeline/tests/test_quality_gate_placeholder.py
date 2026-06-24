from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from services.paper_analysis import has_bad_placeholder, quality_gate


class QualityGatePlaceholderTest(unittest.TestCase):
    def test_allows_unknown_as_domain_term(self):
        self.assertFalse(
            has_bad_placeholder(
                "Semantic-Aware Autonomous Exploration for UAVs in Unknown Indoor Environments"
            )
        )
        self.assertFalse(has_bad_placeholder("面向未知室内环境的无人机探索问题"))

    def test_rejects_placeholder_only_values(self):
        for value in ["Unknown", "未知", "单位: 未知", "N/A", "Not provided"]:
            with self.subTest(value=value):
                self.assertTrue(has_bad_placeholder(value))

    def test_quality_gate_accepts_unknown_environment_paper(self):
        info = {
            "title": "Semantic-Aware Autonomous Exploration for UAVs in Unknown Indoor Environments",
            "authors": "Nguyen Duc-Thien, Ngoc Minh Do",
            "institutions": "University of Engineering and Technology, Vietnam National University",
            "date": "2026-06-21",
        }
        analysis = {
            f"q{i}": "该回答围绕未知室内环境中的无人机自主探索，说明问题、方法和实验结论。"
            for i in range(1, 11)
        }
        analysis["q4"] = (
            "The core idea targets Unknown Indoor Environments by combining semantic mapping "
            "with frontier-based exploration and probabilistic roadmaps."
        )

        ok, errors = quality_gate(
            info,
            analysis,
            "本文研究语义感知的无人机自主探索问题，面向未知室内环境构建可执行的导航与建图流程。",
            uploaded_images=1,
        )

        self.assertTrue(ok, errors)


if __name__ == "__main__":
    unittest.main()
