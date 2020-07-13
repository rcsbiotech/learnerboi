#!/usr/bin/env python

"""
Script made to solve Rosalind Stronghold 6th problem
----------------------------------------------------

From a FASTA file with up to 10 sequences and 1000kb;
compares their GC content, returning the highest
within a 0.001 error deviation.

---------------------------------------------------
rcsilva@unesp.br
"""

# Libraries
import sys
from Bio import SeqIO

# Declaração de variáveis
## Captura do fasta do SeqIO
fasta_records = {};
fasta_gc = {};

## Captura do maior valor
maior_gc = 0;
maior_id = '';

# Parsing fasta file
fasta_fh = open(sys.argv[1], 'r')

""" Seção do SeqIO
# Para cada sequência, exibe o ID e a sequência completa

for record in SeqIO.parse(fasta_fh, "fasta"):
	print(record.id)
	print(record.seq)
"""

# Parseia como dicionário
for entry in SeqIO.parse(fasta_fh, "fasta"):
	
	# Reinicia os valores de GC
	cntG = 0
	cntC = 0

	# Guarda em um dicionário
	fasta_records[entry.id] = entry.seq

	# AT: Exibe as sequências parseadas
	# print(entry.id, "\n", entry.seq, "\n")

	# Conta C e G
	for nucl in entry.seq:
		if nucl == 'G':
			cntG = cntG + 1
		elif nucl == 'C':
			cntC = cntC + 1

	# Calcula o %GC
	this_gcp = (cntC + cntG)/(int(len(entry.seq)))

	# AT: Exibe o conteúdo de GC
	# print('GC decimal: ', 100 * this_gcp)

	# Guarda o %GC para a dita sequência
	fasta_gc[entry.id] = 100 * this_gcp
	
# AT: Testa o dicionário
# print(fasta_gc)


for chave, valor in fasta_gc.items():
	if float(valor) > float(maior_gc):
		maior_gc = valor
		maior_id = chave

print(maior_id, "\n", maior_gc)






















