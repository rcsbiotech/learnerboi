#!/usr/bin/env python

def dna2rna(x):
    ## Inicializa o objeto string de RNA
    rnastring = []

    ## Para cada letra...
    for letter in x:

        ## Se a letra for T:
        if letter == 'T':

            ## Apenda 'U'
            rnastring.append('U')

        else:

            ## Do contrário, apenda a própria letra
            rnastring.append(letter)

            ## Junta sem separadores
            rna_out = ''.join(rnastring)

    ## Resultado RNA
    return(rna_out)

def translate_protein(x):
    ## Inicializa o objeto de proteina
    protein_string = []

    ## Se não for múltiplo de 03, completa com N
    ## Traduz cada trinca
    ## Retorna as trincas traduzidas

    return(protein_out)
