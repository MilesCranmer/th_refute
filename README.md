# Automated theory refute
(Nowhere near complete. This is something I will spend more time on in grad school (Fall 2018-...).)

Python 2.7

Toy program to automatically parse a research paper and test the models.

This programs aims to answer the question: how much of the research process **itself** can we automate?

My hope is that this program could eventually do this live, and output statistics as it goes. Hopefully this program/idea is helpful for the research process -- a lot more could be automated.

Eventually I feel this sort of thing will come of age, but I think it would be interesting if you could demonstrate it *right now* on special cases. 

This program will download a research paper from arxiv, and (eventually) look for testable equations/models, generate some executable equations with `sympy`, search for keywords, automatically download relevant data, do some data reduction, and try a fit.

## Dependencies:

sympy (For storing symbolic models)

astropy, numpy (For computation with units)

urllib2, gzip (For downloading from arxiv)
