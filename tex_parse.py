"""@module This program parses a .tex file for relevant equations."""

import urllib2
from sympy import sympify

def download_tex(arxiv_handle_str, filename='th_refute_intermediate_file'):
    """Download the .tex file for the arxiv handle"""
    base = "http://arxiv.org/e-print/"
    download_string = base+arxiv_handle_str
    response = urllib2.urlopen(download_string)
    tex_source = response.read()
    return tex_source

def parse_tex(tex_source):
	"""Parse tex source code for model descriptions"""
	models = []
	models.append({
		'equation':{
			'symbolic': sympify('x'),
			'description': {
				'returns': 'luminosity',
				'x':'frequency'}
				},
		'source':'frb',
		'keywords': ['radio', 'fast', 'single pulse']
		})
	return models