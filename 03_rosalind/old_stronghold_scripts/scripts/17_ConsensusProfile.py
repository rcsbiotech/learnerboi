#!/usr/bin/env python


"""
-------------------------------------------------------------------------------
Finding a most likely common ancestor


Given: A collection of at most 10 DNA strings of equal length (max 1kbp) 
in FASTA format

Return: A consensus string and profile matrix for the collection (if several
possible consensus strings exist, then you may return any of them

Planejamento do código:

1. Cria um perfil para cada sequência (entry.seq)
    A- Cada perfil possui 04 vetores, para cada nucleotídeo
    B- Cada nucleotídeo deverá somar 01 em algum dos vetores, posicionalmente
    C- Os perfis serão processados em estrutura de lista
-------------------------------------------------------------------------------
"""


# Bibliotecas de seq. fasta
import sys
from Bio import SeqIO

## Abre a sequência fasta (argv[1])
fasta_fh = open(sys.argv[1], 'r')

## Captura o comprimento da sequência
parse = 0
while (parse < 1):
    for entry in SeqIO.parse(fasta_fh, "fasta"):
        first_seq = entry.seq
        parse = parse + 1

first_seq_len = len(first_seq)
#print("Sequence length: ", first_seq_len)

## Cria a lista vazia 'profiles'
profiles = []
profiles_iterator = 0;

## Objeto vazio de lista, deve ter o comprimento da seq. FASTA
while (profiles_iterator < first_seq_len):
    profiles.append(0)
    profiles_iterator = profiles_iterator + 1

#print("Starting object: " , profiles)

#### Loop para montar o perfil de cada sequência ####

## Somador final dos perfis
all_A = profiles.copy()
all_C = profiles.copy()
all_G = profiles.copy()
all_T = profiles.copy()

## Abre a sequência fasta (argv[1])
fasta_fh = open(sys.argv[1], 'r')

for entry in SeqIO.parse(fasta_fh, "fasta"):
    
    ## Auto-teste: funciona da captura
    #print(entry.id)
    # print(entry.seq)
    # print(profiles)
    
    this_A = profiles.copy()
    this_C = profiles.copy()
    this_G = profiles.copy()
    this_T = profiles.copy()
    
    ## Posição do iterador que percorre a sequência
    seq_iterator_posit = 0

    ## Passa por cada letra da sequência, somando em sua lista
    for letter in entry.seq:
        if letter == 'A':
            this_A[seq_iterator_posit] = this_A[seq_iterator_posit] + 1
        if letter == 'C':
            this_C[seq_iterator_posit] = this_C[seq_iterator_posit] + 1
        if letter == 'G':
            this_G[seq_iterator_posit] = this_G[seq_iterator_posit] + 1
        if letter == 'T':
            this_T[seq_iterator_posit] = this_T[seq_iterator_posit] + 1
            
        seq_iterator_posit += 1
        #print(this_A, "\n", this_C, "\n", this_G, "\n", this_T, "\n")
        
    ## Soma o consenso atual com todos os restantes
    
    # Disfuncional: cria apêndices
    # all_A = all_A + this_A
    # all_C = all_C + this_C
    # all_G = all_G + this_G
    # all_T = all_T + this_T
    
    ### Iterador para nuc_A ###
    sum_iter = 0
    for posit in all_A:
        all_A[sum_iter] = all_A[sum_iter] + this_A[sum_iter]
        sum_iter += 1
        
    ### Iterador para nuc_C ###
    sum_iter = 0
    for posit in all_C:
        all_C[sum_iter] = all_C[sum_iter] + this_C[sum_iter]
        sum_iter += 1
        
    ### Iterador para nuc_G ###
    sum_iter = 0
    for posit in all_G:
        all_G[sum_iter] = all_G[sum_iter] + this_G[sum_iter]
        sum_iter += 1
        
    ### Iterador para nuc_T ###
    sum_iter = 0
    for posit in all_T:
        all_T[sum_iter] = all_T[sum_iter] + this_T[sum_iter]
        sum_iter += 1
    
    ## Auto-teste: exibe a soma atual
    #print("Total de A: ", all_A)
    #print("Total de C: ", all_C)
    #print("Total de G: ", all_G)
    #print("Total de T: ", all_T)
    
## Feita a soma, começa a etapa de escrever a nova sequência
nucl_posit = 0
final_seq = profiles.copy()

while nucl_posit < len(all_A):
    #print(nucl_posit)
    
    ## Compara a posição de A com todas as outras,
    ## sendo maior ou igual, o nucleotídeo será A.
    
    if all(all_A[nucl_posit] >= x for x in(
    all_C[nucl_posit],
    all_G[nucl_posit],
    all_T[nucl_posit])):
        
        final_seq[nucl_posit] = 'A'
    
    ## O mesmo para outros nucleotídeos (C, G, T)

    if all(all_C[nucl_posit] >= x for x in(
    all_A[nucl_posit],
    all_G[nucl_posit],
    all_T[nucl_posit])):
        
        final_seq[nucl_posit] = 'C'
        
    ## O mesmo para outros nucleotídeos (G, T)

    if all(all_G[nucl_posit] >= x for x in(
    all_A[nucl_posit],
    all_C[nucl_posit],
    all_T[nucl_posit])):
        
        final_seq[nucl_posit] = 'G'
        
    ## O mesmo para outros nucleotídeos (T)

    if all(all_T[nucl_posit] >= x for x in(
    all_A[nucl_posit],
    all_C[nucl_posit],
    all_G[nucl_posit])):
        
        final_seq[nucl_posit] = 'T'
    
    
    nucl_posit += 1
    
for x in final_seq: 
    print(x, end='')
    
print("\nA:", end=' ')
for x in all_A:
    print(x, end=' ')
    
print("\nC:", end=' ')
for x in all_C:
    print(x, end=' ')
    
print("\nG:", end=' ')
for x in all_G:
    print(x, end=' ')
   
print("\nT:", end=' ')
for x in all_T:
    print(x, end=' ')
    
print("\nFinal do código!\n")
    


