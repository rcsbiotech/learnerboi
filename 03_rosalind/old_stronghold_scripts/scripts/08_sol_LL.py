#!/usr/bin/env python

import sys;

dna_fh = sys.argv[1]
seq1,seq2 = open(dna_fh).read().split('\r\n')
print(seq1, "\n", seq2)
