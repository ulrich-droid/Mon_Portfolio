from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class TestProjectsNavigation(unittest.TestCase):
    def test_projects_page_exists(self):
        self.assertTrue((ROOT / "pages" / "1_tous_les_projets.py").exists())


if __name__ == "__main__":
    unittest.main()
