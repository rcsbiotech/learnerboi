#!/usr/bin/env python

# Necessário para importar arquivos ($ARGV[0] da perl)
import sys

# Argumentos para obter e exportar a resposta
dna_input = sys.argv[1]
#rna_output = sys.argv[2]

# Abre o arquivo
dna_fh = open(dna_input, 'r')

# Captura a string da primeira linha
dnastring = dna_fh.readline()
rnastring = []

for letter in dnastring:
	if letter == 'A':
		rnastring.append('A')
	elif letter == 'T':
		rnastring.append('U')
	elif letter == 'C':
		rnastring.append('C')
	elif letter == 'G':
		rnastring.append('G')
		
rna_out = ''.join(rnastring)
print(rna_out)
