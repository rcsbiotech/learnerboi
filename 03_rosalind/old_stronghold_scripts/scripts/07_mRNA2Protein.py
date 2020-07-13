#!/usr/bin/env python

"""
Translates a file with ONE sequence to +1 protein frame
rc.silva@unesp.br
"""

# Libraries
# sys: to open file from argument (argv[1])
# seqIO: parse fasta sequence
# IUPAC: translate mRNA to protein

import sys
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

# Parsing fasta file
fasta_fh = open(sys.argv[1], 'r')

for line in fasta_fh:

	# Reads and removes newlines as RNA
	nucl = Seq(line.rsplit("\n")[0], IUPAC.unambiguous_rna)

	# Prints the translation
	print(nucl.translate())
	

