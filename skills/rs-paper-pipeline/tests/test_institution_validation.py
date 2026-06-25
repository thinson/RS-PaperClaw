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

    def test_extracts_ieee_thanks_affiliations_from_source(self):
        tex = r"""
        \thanks{This work was supported by the National Natural Science Foundation of China.}
        \thanks{Chuyu Zhong, Bowen Chen, Zhengxia Zou, and Zhenwei Shi are with the Department of Aerospace Intelligent Science and Technology, School of Astronautics, Beihang University, Beijing 100191, China, and also with the Key Laboratory of Spacecraft Design Optimization and Dynamic Simulation Technologies, Ministry of Education, Beihang University, Beijing 100191, China. Qinzhe Yang is with Shen Yuan Honors College, Beihang University, Beijing 100191, China. Keyan Chen is with the College of Computing and Data Science, Nanyang Technological University, Singapore.}
        """
        with tempfile.TemporaryDirectory() as temp_dir:
            source_path = Path(temp_dir) / "source.tar"
            tex_path = Path(temp_dir) / "main.tex"
            tex_path.write_text(tex, encoding="utf-8")
            with tarfile.open(source_path, "w") as archive:
                archive.add(tex_path, arcname="main.tex")

            institutions = extract_institutions_from_latex_source(source_path)

        self.assertIn("School of Astronautics, Beihang University", institutions)
        self.assertIn("Key Laboratory of Spacecraft Design Optimization", institutions)
        self.assertIn("Shen Yuan Honors College, Beihang University", institutions)
        self.assertIn("College of Computing and Data Science, Nanyang Technological University", institutions)
        self.assertNotIn("supported", institutions)

    def test_extracts_neurips_author_block_affiliations_from_source(self):
        tex = r"""
        \author{
        Dimitri Gominski\textsuperscript{1}\!\!\And
        Maurice Mugabowindekwe \textsuperscript{1,2}\!\!\And
        Qiue Xu \textsuperscript{3}\!\!\And
        Loic Landrieu \textsuperscript{6}\!\!\and
        \textsuperscript{1}University of Copenhagen
        \and \textsuperscript{2}University of Rwanda
        \and \textsuperscript{3}University of Chinese Academy of Sciences
        \and \textsuperscript{6}LIGM, CNRS, Univ Gustave Eiffel, ENPC, IPP
        }
        """
        with tempfile.TemporaryDirectory() as temp_dir:
            source_path = Path(temp_dir) / "source.tar"
            tex_path = Path(temp_dir) / "main.tex"
            tex_path.write_text(tex, encoding="utf-8")
            with tarfile.open(source_path, "w") as archive:
                archive.add(tex_path, arcname="main.tex")

            institutions = extract_institutions_from_latex_source(source_path)

        self.assertEqual(
            institutions,
            "University of Copenhagen；University of Rwanda；"
            "University of Chinese Academy of Sciences；"
            "LIGM, CNRS, Univ Gustave Eiffel, ENPC, IPP",
        )

    def test_extracts_ieee_authorblock_affiliations_before_email(self):
        tex = r"""
        \author{
        \IEEEauthorblockA{
        \IEEEauthorrefmark{1}Image Processing Department,
        Fraunhofer ITWM,
        Kaiserslautern, Germany,\\
        \{vladyslav.polushko, ronald.roesch, markus.rauhut\}@itwm.fraunhofer.de
        }
        \IEEEauthorblockA{
        \IEEEauthorrefmark{2}ACIDA Lab,
        Hochschule Darmstadt,
        Darmstadt, Germany.
        \{vladyslav.polushko, thomas.maerz\}@h-da.de
        }
        \IEEEauthorblockA{
        \IEEEauthorrefmark{3}
        Institut f{\"u}r Optische Sensorsysteme, DLR,
        Berlin, Germany,
        tilman.bucher@dlr.de
        }
        }
        """
        with tempfile.TemporaryDirectory() as temp_dir:
            source_path = Path(temp_dir) / "source.tar"
            tex_path = Path(temp_dir) / "main.tex"
            tex_path.write_text(tex, encoding="utf-8")
            with tarfile.open(source_path, "w") as archive:
                archive.add(tex_path, arcname="main.tex")

            institutions = extract_institutions_from_latex_source(source_path)

        self.assertIn("Image Processing Department, Fraunhofer ITWM", institutions)
        self.assertIn("ACIDA Lab, Hochschule Darmstadt", institutions)
        self.assertIn("Institut für Optische Sensorsysteme, DLR", institutions)
        self.assertNotIn("@", institutions)

    def test_extracts_ieee_while_and_now_with_affiliations(self):
        tex = r"""
        \thanks{Zhongcheng Hong completed this work while with The Hong Kong University of Science and Technology (Guangzhou), Guangzhou, China, and is now with Auckland University of Technology, Auckland, New Zealand (e-mail: zhongcheng.hong@autuni.ac.nz).}
        \thanks{Ying-Cong Chen and Hui Xiong are also with the Department of Computer Science and Engineering, The Hong Kong University of Science and Technology, Hong Kong SAR, China.}
        """
        with tempfile.TemporaryDirectory() as temp_dir:
            source_path = Path(temp_dir) / "source.tar"
            tex_path = Path(temp_dir) / "main.tex"
            tex_path.write_text(tex, encoding="utf-8")
            with tarfile.open(source_path, "w") as archive:
                archive.add(tex_path, arcname="main.tex")

            institutions = extract_institutions_from_latex_source(source_path)

        self.assertIn("The Hong Kong University of Science and Technology (Guangzhou)", institutions)
        self.assertIn("Auckland University of Technology", institutions)
        self.assertIn("Department of Computer Science and Engineering", institutions)
        self.assertNotIn("completed this work", institutions)

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

    def test_extracts_science_china_address_affiliations_from_source(self):
        tex = r"""
        \author[1]{Qinzhe YANG}{}
        \author[1,2,3]{Chenyang LIU}{}
        \author[4]{Jia XU}{}
        \address[1]{Shen Yuan Honors College, Beihang University, Beijing {\rm 100191}, China}
        \address[2]{Department of Aerospace Intelligent Science and Technology, School of Astronautics, Beihang University, Beijing {\rm 100191}, China}
        \address[3]{State Key Laboratory of Virtual Reality Technology and Systems, Beihang University, Beijing {\rm 100191}, China}
        \address[4]{Qian Xuesen Laboratory of Space Technology, China Academy of Space Technology, Beijing {\rm 100094}, China}
        """
        with tempfile.TemporaryDirectory() as temp_dir:
            source_path = Path(temp_dir) / "source.tar"
            tex_path = Path(temp_dir) / "paper.tex"
            tex_path.write_text(tex, encoding="utf-8")
            with tarfile.open(source_path, "w") as archive:
                archive.add(tex_path, arcname="SCIS-2021-1065.tex")

            institutions = extract_institutions_from_latex_source(source_path)

        self.assertIn("Shen Yuan Honors College, Beihang University", institutions)
        self.assertIn("Qian Xuesen Laboratory of Space Technology", institutions)
        self.assertTrue(is_valid_institution_text(institutions))

    def test_extracts_springer_institute_and_skips_project_page(self):
        tex = r"""
        \institute{ \textsuperscript{1}Gwangju Institute of Science
        and Technology, Gwangju, Republic of Korea\\
        \textsuperscript{2}GIST InnoCORE AI-Nano Convergence Institute for Early Detection of Neurode-
        generative Diseases, Gwangju Institute of Science and Technology, 61005 Gwangju, Republic of Korea \\
        \email{kjw01124@gm.gist.ac.kr, hbk08101@gm.gist.ac.kr, uehwan@gist.ac.kr} \\[0.2em]
        \small\textbf{Project Page:} \texttt{\url{https://github.com/AutoCompSysLab/C3-Bench}}}
        """
        with tempfile.TemporaryDirectory() as temp_dir:
            source_path = Path(temp_dir) / "source.tar"
            tex_path = Path(temp_dir) / "main.tex"
            tex_path.write_text(tex, encoding="utf-8")
            with tarfile.open(source_path, "w") as archive:
                archive.add(tex_path, arcname="main.tex")

            institutions = extract_institutions_from_latex_source(source_path)

        self.assertIn("Gwangju Institute of Science and Technology", institutions)
        self.assertIn("GIST InnoCORE AI-Nano Convergence Institute", institutions)
        self.assertNotIn("Project Page", institutions)
        self.assertNotIn("github", institutions)
        self.assertTrue(is_valid_institution_text(institutions))

    def test_extracts_ieee_thanks_without_contribution_note(self):
        tex = r"""
        \thanks{The work was supported by the National Natural Science Foundation of China under Grant 62125102.}
        \thanks{Qinzhe Yang is with Shen Yuan Honors College, Beihang University, Beijing 100191, China.
        Keyan Chen, Zhenwei Shi, and Zhengxia Zou are with the Department of Aerospace Intelligent Science and Technology, School of Astronautics, and with the State Key Laboratory of Virtual Reality Technology and Systems, Beihang University, Beijing 100191, China.
        Jia Xu is with the Qian Xuesen
        Laboratory of Space Technology, China Academy of Space Technology,
        Beijing 100094, China. $^\dag$ These authors contributed equally to this paper.}
        """
        with tempfile.TemporaryDirectory() as temp_dir:
            source_path = Path(temp_dir) / "source.tar"
            tex_path = Path(temp_dir) / "main.tex"
            tex_path.write_text(tex, encoding="utf-8")
            with tarfile.open(source_path, "w") as archive:
                archive.add(tex_path, arcname="main.tex")

            institutions = extract_institutions_from_latex_source(source_path)

        self.assertIn("Shen Yuan Honors College, Beihang University", institutions)
        self.assertIn("Department of Aerospace Intelligent Science and Technology", institutions)
        self.assertIn("State Key Laboratory of Virtual Reality Technology and Systems", institutions)
        self.assertIn("Qian Xuesen Laboratory of Space Technology", institutions)
        self.assertNotIn("contributed", institutions)
        self.assertNotIn("supported", institutions)
        self.assertTrue(is_valid_institution_text(institutions))

    def test_extracts_ieee_compsoc_itemized_thanks(self):
        tex = r"""
        \author{Qinzhe~Yang, Dongyu~Wang, Haohan~Niu,~Jia~Xu,\\Zhenwei~Shi, and~Zhengxia~Zou
        \IEEEcompsocitemizethanks{
        \IEEEcompsocthanksitem Qinzhe Yang and Haohan Niu are with Shen Yuan Honors College, Beihang University, Beijing 100191, China.
        \IEEEcompsocthanksitem Dongyu Wang, Zhenwei Shi, and Zhengxia Zou are with the Department of Aerospace Intelligent Science and Technology, School of Astronautics, and with the State Key Laboratory of Virtual Reality Technology and Systems, Beihang University, Beijing 100191, China.
        \IEEEcompsocthanksitem Jia Xu is with the Qian Xuesen
        Laboratory of Space Technology, China Academy of Space Technology,
        Beijing 100094, China.
        \IEEEcompsocthanksitem The work was supported by the National Natural Science Foundation of China.
        }}
        """
        with tempfile.TemporaryDirectory() as temp_dir:
            source_path = Path(temp_dir) / "source.tar"
            tex_path = Path(temp_dir) / "main.tex"
            tex_path.write_text(tex, encoding="utf-8")
            with tarfile.open(source_path, "w") as archive:
                archive.add(tex_path, arcname="main.tex")

            institutions = extract_institutions_from_latex_source(source_path)

        self.assertIn("Shen Yuan Honors College, Beihang University", institutions)
        self.assertIn("Department of Aerospace Intelligent Science and Technology", institutions)
        self.assertIn("State Key Laboratory of Virtual Reality Technology and Systems", institutions)
        self.assertIn("Qian Xuesen Laboratory of Space Technology", institutions)
        self.assertNotIn("Qinzhe Yang", institutions)
        self.assertNotIn("supported", institutions)
        self.assertTrue(is_valid_institution_text(institutions))


if __name__ == "__main__":
    unittest.main()
