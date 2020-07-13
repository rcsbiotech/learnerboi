#!/usr/bin/env python

import sys

# Read the file with DNA string
dna_file = sys.argv[1];
dna_fh = open(dna_file, 'r')

# Init variables
# Counts of A, T, C, G
cnt_a = 0;
cnt_t = 0;
cnt_c = 0;
cnt_g = 0;

for letter in dna_fh.readline().rstrip('\n'):
	if letter == 'A':
		cnt_a = cnt_a + 1;
	elif letter == 'T':
		cnt_t = cnt_t + 1;
	elif letter == 'C':
		cnt_c = cnt_c + 1;
	elif letter == 'G':
		cnt_g = cnt_g + 1;

print(cnt_a, ' ', cnt_c, ' ', cnt_g, ' ', cnt_t, ' ')

