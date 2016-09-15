"""@module This program currently holds unit tests for th_refute"""

import unittest
from tex_parse import download_tex, parse_tex, clean_tex

TEST_MODEL = "1401.6674"

def run_all():
	unittest.main()

class TestTexDownload(unittest.TestCase):
	"""Test the functionality of the tex downloading"""
	def setUp(self):
		"""Download the tex source"""
		self.tex_source = download_tex(TEST_MODEL)

	def test_throughput(self):
		"""Test that we are getting tex source code"""
		self.assertTrue(isinstance(self.tex_source, type("string")))
		self.assertGreater(len(self.tex_source), 1000)

	def test_latex(self):
		"""Test that there is actual latex"""
		self.assertTrue(self.tex_source.find('documentclass') != -1)

	def test_equations(self):
		"""Make sure there are many equations"""
		self.assertGreater(
			clean_tex(self.tex_source).count("\\begin{equation}"),
			5)

class TestTexParse(unittest.TestCase):
    """Test the functionality of the tex parsing"""
    def test_throughput(self):
        """Test that a list of models (dictionaries) is returned"""
        models = parse_tex(download_tex(TEST_MODEL))
        self.assertTrue(isinstance(models, list))
        self.assertTrue(isinstance(models[0], dict))

if __name__ == '__main__':
	unittest.main()