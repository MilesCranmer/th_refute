"""@module This program currently holds unit tests for th_refute"""

import unittest
from tex_parse import download_tex, parse_tex

TEST_MODEL = "1401.6674"

def run_all():
	unittest.main()

class TestTexDownload(unittest.TestCase):
	"""Test the functionality of the tex downloading"""
	def test_throughput(self):
		"""Test that we are getting tex source code"""
		tex_source = download_tex(TEST_MODEL)
		self.assertTrue(isinstance(tex_source, type("string")))
		self.assertGreater(len(tex_source), 1000)

class TestTexParse(unittest.TestCase):
    """Test the functionality of the tex parsing"""
    def test_throughput(self):
        """Test that a list of models (dictionaries) is returned"""
        models = parse_tex(download_tex(TEST_MODEL))
        self.assertTrue(isinstance(models, list))
        self.assertTrue(isinstance(models[0], dict))

if __name__ == '__main__':
	unittest.main()