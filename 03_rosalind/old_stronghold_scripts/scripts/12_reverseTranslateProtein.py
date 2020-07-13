#!/usr/bin/env python

"""
Rosalind Challenge 12. Reverse translation
-------------------------------------------------------------------------

- From a protein sequence, gives the number of possible reverse
translations, by a modulo of 1kk
-------------------------------------------------------------------------

rc.silva@unesp.br
"""

# Libraries
import sys

# Captura as duas sequências
prot_fh = open(sys.argv[1], 'r')

# Final AA value
var_aa = 1

# Captures protein sequence
prot = prot_fh.readline().rsplit("\n")[0]

# Loops for possibilites
for char in prot:
	if char == "M":
		var_aa = var_aa * 1
	elif char == "A":
		var_aa = var_aa * 4
	elif char == "F":
		var_aa = var_aa * 2
	elif char == "L":
		var_aa = var_aa * 6
	elif char == "I":
		var_aa = var_aa * 3
	elif char == "V":
		var_aa = var_aa * 4
	elif char == "S":
		var_aa = var_aa * 6
	elif char == "P":
		var_aa = var_aa * 4
	elif char == "T":
		var_aa = var_aa * 4
	elif char == "Y":
		var_aa = var_aa * 2
	elif char == "H":
		var_aa = var_aa * 2
	elif char == "Q":
		var_aa = var_aa * 2
	elif char == "N":
		var_aa = var_aa * 2
	elif char == "K":
		var_aa = var_aa * 2
	elif char == "D":
		var_aa = var_aa * 2
	elif char == "E":
		var_aa = var_aa * 2
	elif char == "C":
		var_aa = var_aa * 2
	elif char == "R":
		var_aa = var_aa * 6
	elif char == "G":
		var_aa = var_aa * 4
		
# Adds stop codon
var_aa = var_aa * 3

# Takes modulo
mod_aa = var_aa % 1000000

print("Modulo is: ", mod_aa)
	
