#!/usr/bin/env python

"""
Rosalind Challenge 14. Calculates protein mass
-------------------------------------------------------------------------
From a protein sequence, calculate its monoisotopic mass
-------------------------------------------------------------------------

rc.silva@unesp.br
"""

# Libraries
import sys

# Captura as duas sequências
prot_fh = open(sys.argv[1], 'r')

# Final AA value
var_aa = 0

# Captures protein sequence
prot = prot_fh.readline().rsplit("\n")[0]

# Loops for possibilites
for char in prot:
	if char == "M":
		var_aa = var_aa + 131.04049
	elif char == "W":
		var_aa = var_aa + 186.07931
	elif char == "A":
		var_aa = var_aa + 71.03711
	elif char == "F":
		var_aa = var_aa + 147.06841
	elif char == "L":
		var_aa = var_aa + 113.08406
	elif char == "I":
		var_aa = var_aa + 113.08406
	elif char == "V":
		var_aa = var_aa + 99.06841
	elif char == "S":
		var_aa = var_aa + 87.03203
	elif char == "P":
		var_aa = var_aa + 97.05276
	elif char == "T":
		var_aa = var_aa + 101.04768
	elif char == "Y":
		var_aa = var_aa + 163.06333
	elif char == "H":
		var_aa = var_aa + 137.05891
	elif char == "Q":
		var_aa = var_aa + 128.05858
	elif char == "N":
		var_aa = var_aa + 114.04293
	elif char == "K":
		var_aa = var_aa + 128.09496
	elif char == "D":
		var_aa = var_aa + 115.02694
	elif char == "E":
		var_aa = var_aa + 129.04259
	elif char == "C":
		var_aa = var_aa + 103.00919
	elif char == "R":
		var_aa = var_aa + 156.10111
	elif char == "G":
		var_aa = var_aa + 57.02146

print("Final mass is: ", var_aa)
	
