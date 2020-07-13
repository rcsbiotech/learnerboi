#!/usr/bin/env python

# Necessário para importar arquivos
import sys

# Capturar o arquivo
dna_input = sys.argv[1]
dna_fh = open(dna_input, 'r')

# Captura a string da primeira linha
dnastring = dna_fh.readline()
dna_compl = []

for letter in dnastring:
        if letter == 'A':
                dna_compl.append('T')
        elif letter == 'T':
                dna_compl.append('A')
        elif letter == 'C':
                dna_compl.append('G')
        elif letter == 'G':
                dna_compl.append('C')

# Inverte a string: built-in da função slice (begin:step:order)                
dna_compl_ordered = dna_compl[::-1]
dna_compl_ordered = ''.join(dna_compl_ordered)

# Output
print(dna_compl_ordered)
