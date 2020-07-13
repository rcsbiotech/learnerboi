#!/usr/bin/env python

"""
-------------------------------------------------------------------------------
Rosalind Problem No: 16
Title: Finding a Protein Motif.

To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as N{P}[ST]{P}.

You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt database, by inserting the ID number into

http://www.uniprot.org/uniprot/uniprot_id

Alternatively, you can obtain a protein sequence in FASTA format by following

http://www.uniprot.org/uniprot/uniprot_id.fasta

For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.
-------------------------------------------------------------------------------
rc.silva@unesp.br
"""

# Libraries
import sys
from Bio import SeqIO

# Variables
## Inicializa o dicionário de nucleotídeos FASTA;
fasta_records = {}

# Input fasta file (argv[1])
fasta_fh = open(sys.argv[1], 'r')

# Captura os fastas como dicionário
for entry in SeqIO.parse(fasta_fh, "fasta"):
	fasta_records[entry.id] = entry.seq

