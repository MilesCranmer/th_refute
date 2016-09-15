"""@module This program currently holds unit tests for th_refute"""

import unittest
from tex_parse import download_tex, parse_tex, clean_tex
from astropy import units as u

TEST_MODEL = "1401.6674"

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
		#TODO: Demand more from this clean_tex function!

class TestTexParse(unittest.TestCase):
    """Test the functionality of the tex parsing"""
    def setUp(self):
    	"""Load model"""
        self.models = parse_tex(download_tex(TEST_MODEL))
    def test_throughput(self):
        """Test that a list of models (dictionaries) is returned"""
        self.assertTrue(isinstance(self.models, list))
        self.assertTrue(isinstance(self.models[0], dict))
    def test_model(self):
    	"""Test that we can simulate with the model given"""
    	self.assertTrue(isinstance(
    		float(self.models[0]['equation']['symbolic'].evalf(subs={'v':50e6})),
    		float))

class TestParkesDownload(unittest.TestCase):
	"""Test downloading of parkes data"""
	def test_throughput(self):
		"""Test that we can download anything at all"""
		pass

if __name__ == '__main__':
	unittest.main()