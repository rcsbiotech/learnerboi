#!/usr/bin/env python

"""
Rosalind Challenge 9. Calculate Hammond Distance

- Finds the number of point mutations between two EQUAL sized sequences
(up to 1kb), and counts all point mutations between them
--------------------------------------------------------------------------

rc.silva@unesp.br
"""

# Libraries
import sys

# Captura as duas sequências
seq_fh = open(sys.argv[1], 'r')
line_cnt = 0

# Captura as sequências por newline
for line in seq_fh:
	if line_cnt == 0:
		seq1 = line.rsplit("\n")[0]
	if line_cnt == 1:
		seq2 = line.rsplit("\n")[0]

	# Aumenta o contador
	line_cnt = line_cnt + 1

# Exibe as sequências
print("\n>FASTA1\n",seq1,"\n>FASTA2\n", seq2)

# Calcula o score
hscore = 0
starter = 0

for char in seq1:
	if str(char) != str(seq2[starter]):
		hscore = hscore + 1
	starter = starter + 1
		
print("\nFinal Hammond/mismatches score: ", hscore)
			
