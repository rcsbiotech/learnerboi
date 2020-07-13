#!/usr/bin/env python

"""
Code made to solve the 10th Rosalind Stronghold problem
-------------------------------------------------------------------------------
Given: Six nonnegative integers, each of which does not exceed 20,000. 
The integers correspond to the number of couples in a population possessing
each genotype pairing for a given factor. In order, the six given integers 
represent the number of couples having the following genotypes:

    AA-AA
    AA-Aa
    AA-aa
    Aa-Aa
    Aa-aa
    aa-aa

Return: The expected number of offspring displaying the dominant phenotype in 
the next generation, under the assumption that every couple has exactly two 
offspring.
-------------------------------------------------------------------------------
rcsilva@unesp.br
"""

# Libraries
import sys

# Steps
# 1. Parse input file
# 2. Iterate over numbers to generate 2 offspring per class

parents_fh = open(sys.argv[1], 'r')

# AT: captura dos valores
# print(parents_fh.read())

# Captura os fenótipos
DD, DH, DR, HH, HR, RR = parents_fh.read().split(' ')
RR = RR.rsplit("\n")[0]

# Exibe os fenótipos:
print("-------------------------------------------------------")
print("Pares duplo dominante, ou DD: ", DD)
print("Pares dominante-heterozigotos, ou DH: ", DH)
print("Pares dominante-recessivo, ou DR: ", DR)
print("Pares duplo-hetero, ou HH: ", HH)
print("Pares hetero-recessivo, ou RR: ", RR)
print("-------------------------------------------------------")

# Cálculo do número esperado (Expected Offspring, var_EO):

var_EO = \
		int(DD) * 2.00 + \
		int(DH) * 2.00 + \
		int(DR) * 2.00 + \
		int(HH) * 1.50 + \
		int(HR) * 1.00 + \
		int(RR) * 0.00

print("Filiação esperada: ", var_EO, "de fenótipos dominantes.")







