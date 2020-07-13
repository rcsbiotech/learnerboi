#!/usr/bin/env python

import sys
import regex as re

"""
Finds and gives all substring positions of a small string (like a DNA motif)
in a large (up to 1kb) sequence, and returns all positions separated by 
spaces, in a 1-based numbering schema
"""

cnt = 1;
seq_fh = open(sys.argv[1], 'r')

for line in seq_fh:
	
	# Captura a expressão
	if cnt == 1:
		expr = line.rsplit("\n")[0]
	
	# Captura o padrão
	if cnt == 2:
		patt = line.rsplit("\n")[0]

	cnt = cnt + 1

# Exibe os resultados do laço
print(str(expr), str(patt))

# Captura com overlap
matches = re.finditer(patt, expr, overlapped=True)
mt_coords = []

# Exibe o match
for match in matches: 
	# print(match)
	newmatch = int((match.span()[0])) + 1
	mt_coords.append(newmatch)
	# print(match.group()
	
for x in mt_coords:
	print(x, end=' ')

print("\nEnd of code.\n")


