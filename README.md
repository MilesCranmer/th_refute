# th_refute
Python 2.7
Toy program to automatically parse a research paper and test the models against data.

This programs aims to answer the question: much of the research process *itself* can we automate?
Eventually I feel this sort of thing will come of age, but I think it would be interesting if you could demonstrate it on special cases. 

This program will download a research paper, and (eventually) look for testable equations/models, metaprogram a test script, automatically download relevant data, and try a fit.

## Dependencies:

sympy (For storing symbolic models)
astropy, numpy (For computation with units)
urllib2, gzip (For downloading from arxiv)