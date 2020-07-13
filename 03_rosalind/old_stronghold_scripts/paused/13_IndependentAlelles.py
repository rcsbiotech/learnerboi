#!/usr/bin/env python


"""
Code made to solve the 13th Rosalind Stronghold problem
-------------------------------------------------------------------------------
Recebendo dois inteiros positivos, k \le 7 e  N \le 2^k, retornar a probabilidade de existirem ao menos N indivíduos de genótipo AaBb somente na geração k da árvore da família. Assumir que o problema começa com Toninho, que na geração 0 tem o genótipo Aa Bb, e na passagem de cada geração são gerados dois filhos. Todos os organismos sempre tem um par de genótipo AaBb.
-------------------------------------------------------------------------------
rcsilva@unesp.br
"""

# Libraries
import sys

# Steps
# 1. Parse input file
# 2. Iterate over numbers to generate 2 offspring per class

data_fh = open(sys.argv[1], 'r')

# Captura os fenótipos
k, n = data_fh.read().split(' ')
n = int(n.rsplit("\n")[0])
k = int(k)

print("Número de gerações (k): ", k)
print("Número de indivíduos esperados (n): ", n)

print("Chance de não haver nenhum indivíduo HT: ", 0.75 ** (k+1))
print("Chance de haver exatamento um indivíduo HT: ", 0.25 ** (k+1))

# Começa com 0 indivíduos
n_ind = 0
cnt = 0
n_final = k ** 2

while n_final >= 1:
	n_ind = n_ind + ((0.25 ** ((k ** 2) - cnt)) * (0.75 ** (0 + cnt)))
	n_final = n_final - 1
	cnt = cnt + 1
	
print("Probabilidade de obter esse número de indivíduos: ", n_ind)
