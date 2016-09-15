"""@module This program parses a .tex file for relevant equations."""

import urllib2
import StringIO
import gzip
from sympy import sympify

def download_tex(arxiv_handle_str, filename='th_refute_intermediate_file'):
    """Download the .gz file for the arxiv handle.
    	This should only contain a .tex file"""
    base = "http://arxiv.org/e-print/"
    download_string = base+arxiv_handle_str

    response = urllib2.urlopen(download_string)
    compressed_file = StringIO.StringIO()
    compressed_file.write(response.read())
    compressed_file.seek(0)
    decompressed_file = gzip.GzipFile(fileobj=compressed_file, mode='rb')

    tex_source = decompressed_file.read()
    assert tex_source.find('documentclass') != -1
    return tex_source

def apply_newcommands(tex_source):
	"""Apply macros to tex file"""
	tex_source = tex_source.replace("\\eqb", "\\begin{equation}")
	tex_source = tex_source.replace("\\eqe", "\\end{equation}")
	return tex_source

def clean_tex(tex_source):
	"""Clean up the tex file for parsing"""
	return apply_newcommands(tex_source)

def parse_tex(tex_source):
	"""Parse tex source code for model descriptions"""
	tex_source = tex_source
	models = []
	models.append({
		'equation':{
			'symbolic': sympify('v^-2'),
			'description': {
				'returns': 'luminosity',
				'v':'frequency'}
				},
		'source':'frb',
		'keywords': ['radio', 'fast', 'single pulse']
		})
	return models

TEST_MODEL = "1401.6674"
