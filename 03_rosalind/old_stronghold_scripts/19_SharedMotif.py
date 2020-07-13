#!/usr/bin/env python3

"""
-----------------------------------------------------------------------------
A common substring of a collection of strings is a substring of 
every member of the collection. We say that a common substring 
is a longest common substring if there does not exist a longer 
common substring. For example, "CG" is a common substring of "ACGTACGT" and 
"AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a 
longest common substring of "ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique; for a 
simple example, "AA" and "CC" are both longest common substrings of 
"AACC" and "CCAA".

Given: A collection of k (k≤100) DNA strings of length at 
most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. 
(If multiple solutions exist, you may return any single solution.)

http://rosalind.info/problems/lcsm/
-----------------------------------------------------------
rcs.biotec@gmail.com
"""

## Bibliotecas comuns de FASTA
import sys                      ## Para leitura de arquivos
from Bio import SeqIO           ## Para captura de arquivos FASTA
from Bio.Seq import Seq         ## Processamento de sequências

## Abre o arquivo
# fasta_fh = open(sys.argv[1], 'r')
fasta_fh = open("19_SharedMotif.py", 'r')
print(fasta_fh)

## Captura a sequência única
sequence = SeqIO.read(fasta_fh, "fasta")
strseq = str(sequence.seq)
