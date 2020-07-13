#!/usr/bin/env python

"""
-------------------------------------------------------------------------------
18 - Open Reading Frames
http://rosalind.info/problems/orf/

Given: A DNA string s of length at most 1kbp in FASTA format
Return: Every distinct candidate protein string that can be translated from 
ORFs of s, in any order.

Information     DNA             RNA
Start codon     ATG             AUG
Stop codon      TAG,TGA,TAA     UAG,UGA,UAA
-------------------------------------------------------------------------------

"""

## Bibliotecas
import sys                      ## Para leitura de arquivos
from Bio import SeqIO           ## Para captura de arquivos FASTA
from Bio.Seq import Seq         ## Processamento de sequências
from Bio.Alphabet import IUPAC  ## Tradução de DNA em proteínas
import regex as re              ## Para buscar padrões (regex)

## Minhas bibliotecas
from rcsilva import dna2rna

## Verifica se é float
def isfloat(x):
    try:
        float(x)
        return True
    except:
        return False
        
## Pica strings 3 por 3
def split(str, num):
    return [ str[start:start+num] for start in range(0, len(str), num) ]
    
## Faz o reverso complementar (3' -> 5')
def revcomp(str):
    str_start = str[::-1]
    revcomp = ""
    for nucl in str_start:
        if nucl == "A":
            revcomp = revcomp + "T"
        elif nucl == "T":
            revcomp = revcomp + "A"
        elif nucl == "C":
            revcomp = revcomp + "G"
        elif nucl == "G":
            revcomp = revcomp + "C"
    return(revcomp)
    
# Itens únicos
def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    # print list 
    for x in unique_list: 
        print(x)

## Abre o arquivo
fasta_fh = open(sys.argv[1], 'r')

## Captura a sequência única
sequence = SeqIO.read(fasta_fh, "fasta")
strseq = str(sequence.seq)

## Guarda os frames ##
frames = {
    "F1" : strseq,
    "F2" : strseq[1::],
    "F3" : strseq[2::],
    "R1" : revcomp(strseq),
    "R2" : revcomp(strseq)[1::],
    "R3" : revcomp(strseq)[2::]
}

## Guarda as ORFs
possible_orfs = []

## Índice da lista que guarda as sequências
starting_orf = 0

## Flag para limpar a lista a cada passagem
starting_point_flag = 0

## Navega códon a códon, frame a frame
for frame, seq in frames.items():
    #print("frame is: ", frame)
    #print("seq is: ", seq)
    flag_coding = 0
    
    ## Limpa as ORFs caso já seja uma segunda passagem
    if starting_point_flag == 1:
        possible_orfs.append("")
        possible_orfs[starting_orf] = ""
    
    ## Para cada codon
    for string in split(frames[frame], 3):
        ## Se for trinca
        ## Se for starting, começa o codificante
      
        if string == "ATG":
            # print("It is coding!")
            ## Declara codificante
            flag_coding = 1
            ## Inicializa uma nova possível ORF
            possible_orfs.append("")
            starting_point_flag = 1
        
        # Enquanto codificante, guarde as ORFs
        if flag_coding > 0:
            # print("ORF: ", starting_orf)
            possible_orfs[starting_orf] = possible_orfs[starting_orf] + string
        
        # Se chegar em um STOP codon, desmarque codificante
            if string == "TAG" or string == "TGA" or string == "TAA":
                flag_coding = 0
                starting_orf = starting_orf + 1
              
        # Se não for trinca, saia do for
        if len(string) < 3:
            flag_coding = 0
            break
    
            
## Processa as ORFs:
    ## Cria suborfs de ORFS com + de uma metionina
clean_orfs = []
for orf in possible_orfs:
    #print(orf)
    for match in re.finditer('ATG', orf, overlapped=True):
        s = match.start()
        neworf = orf[s:len(orf)]
        #print(neworf)
        clean_orfs.append(neworf)
        
# print(*clean_orfs)

## Guarda as proteínas
proteins = []

for orf in clean_orfs:
    if orf:
        #print("ORF: ", orf)
        RNA = dna2rna(orf)
        prot = Seq(RNA, IUPAC.unambiguous_rna)
        prot_final = prot.translate()
        prot_final = prot_final[:-1]
        proteins.append(prot_final)
        
# Filtra as proteínas com STOP no meio
proteins_clean = []
for seq in proteins:
    strseq = str(seq)
    if not re.search("\*", strseq):
        proteins_clean.append(strseq)

# Finalmente, dá a saída
repeats = []

for prot in proteins_clean:
    if prot not in repeats:
        print(prot)
    else:
        repeats.append(prot)



# ## F1
# for match in re.finditer(r"ATG[A-Z]*(?=(TAG|TGA|TAA))", frames["F1"], overlapped=True):
    # s = match.start() + 1
    # SF1.append(s)

# for match in re.finditer(r"(TAG|TGA|TAA)", frames["F1"], overlapped=True):
    # s = match.start() + 1
    # EF1.append(s)
    
# ## F2
# for match in re.finditer(r"ATG[A-Z]*(?=(TAG|TGA|TAA))", frames["F2"], overlapped=True):
    # s = match.start() + 1
    # SF2.append(s)

# for match in re.finditer(r"(TAG|TGA|TAA)", frames["F2"], overlapped=True):
    # s = match.start() + 1
    # EF2.append(s)
    
# ## F3
# for match in re.finditer(r"ATG[A-Z]*(?=(TAG|TGA|TAA))", frames["F3"], overlapped=True):
    # s = match.start() + 1
    # SF3.append(s)

# for match in re.finditer(r"(TAG|TGA|TAA)", frames["F3"], overlapped=True):
    # s = match.start() + 1
    # EF3.append(s)
    
# print(frames["F1"])
# print(SF1)
# print(EF1)

# print(frames["F2"])
# print(SF2)
# print(EF2)

# print(frames["F3"])
# print(SF3)
# print(EF3)

""" 
Seleciona por posição de splice:
"""

# finish_pos = 0
## Para cada posição de start
# for spos in start_pos:
    
    # ## Para cada posição de finish
    # for epos in end_pos:
        
        # ## Se houverem ao menos 3 NTs;
        # ## Se for a primeira ORF válida;
        # if epos-spos > 2 and finish_pos == 0:
            # print(strseq[spos-1:epos+2])
            # nucl = dna2rna(strseq[spos-1:epos-1])
            # nucl = Seq(nucl, IUPAC.unambiguous_rna)
            # # print(nucl)
            # # print(nucl.translate())
            
            # finish_pos = finish_pos + 1
        
    # finish_pos = 0
    
# test = Seq(dna2rna(strseq), IUPAC.unambiguous_rna)
# print(test.translate())
   

""" Old version
Splitting by ATG, my guess is a regex + splice is better

# ## Separa (split) por cada códon de start
# possible_orfs = re.split("ATG", string_seq)

# ## Auto-teste: Todas as ORFs
# # print(possible_orfs)
# possible_orfs = possible_orfs[1:]

# #print(*possible_orfs)

# ## Problema: Devem ser múltiplos de três
# pos_orfs_posit = 0

# for sequence in possible_orfs:

    # sequence = str(sequence)
    
    # # Auto-teste: tamanho da sequência
    # # Verifica se é multiplo de 3
    # #print("Original seq length: ", len(sequence))
    # #print("Length/3: ", len(sequence)/3)
    # size = len(sequence)
    
    # # Verifica se é int ou float
    # while size % 3 != 0:
        # # print("Modulus is: ", size % 3)
        # sequence = sequence[:-1]
        # size = len(sequence)
        # possible_orfs[pos_orfs_posit] = sequence
        # # print("New size is: ", size)
        # # print("New sequence is: ", sequence)
        
    # # Avança a posição
    # pos_orfs_posit += 1  
    
# # print(possible_orfs)
# ## Após a tradução para RNA (função própria), traduza em proteína
 
# for seq_string in possible_orfs:
    # rna_string = dna2rna(seq_string)
    # print(rna_string)
    # #nucl = "AUG" + Seq(rna_string, IUPAC.unambiguous_rna)
    # #print(nucl.translate())
"""

