#!/usr/bin/env python

# Bibliotecas

## Processamento de texto <- URL
from bs4 import BeautifulSoup
from itertools import groupby

## Abrindo arquivos do sistema
import sys

## Expressões regulares
import regex as re

## Para processamento de sequências fasta
from urllib.request import urlopen

# Rosalind Problem 16: rcsilva

""" Finding a Protein Motif

To allow for the presence of its varying forms, a protein motif is 
represented by a shorthand as follows: [XY] means "either X or Y" and {X}
means "any amino acid except X." For example, the N-glycosylation motif is
written as N{P}[ST]{P}.

You can see the complete description and features of a particular protein by
its access ID "uniprot_id" in the UniProt database, by inserting the ID number
into http://www.uniprot.org/uniprot/uniprot_id

Alternatively, you can obtain a protein sequence in FASTA format by following
http://www.uniprot.org/uniprot/uniprot_id.fasta

For example, the data for protein B5ZC00 can be found at 
http://www.uniprot.org/uniprot/B5ZC00.

------------------------------------------------------------------------------
Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its
given access ID followed by a list of locations in the protein string where
the motif can be found.
-----------------------------------------------------------------------------
Planejamento do código:
    1. Obter sequências FASTAs a partir da lista de IDs;
    2. Realizar o parse das sequências com Biopython;
    3. Implementar a função de busca de motifs;
    4. Rodar a função sobre cada fasta, gerando relatório


Seção de teste: abrindo a URL do Uniprot
------------------------------------------------------------------------------
## Obter uma página de exemplo
url = 'https://www.uniprot.org/uniprot/A2Z669.fasta'

### Abre como HTML
html = urlopen(url)

### Parseia o HTML
soup = BeautifulSoup(html, 'html.parser')

### Extrai o texto
fasta = soup.get_text()

### Exibe o fasta
print(fasta)
------------------------------------------------------------------------------


Método base da Python
------------------------------------------------------------------------------
 for line in urlopen('https://www.uniprot.org/uniprot/A2Z669.fasta'):
    print(line)
    fasta_data = str(line.read(), 'latin')
    print(fasta_data)
    # print(line.rstrip().rstrip("'").lstrip("b").lstrip("'"))
------------------------------------------------------------------------------

## Processando com SeqIO
seq_parsed = SeqIO.parse(fasta, "fasta")
print(seq_parsed)

fasta_header = fasta.rstrip().lstrip().split('\n')[0]
fasta_sequence = fasta.rstrip().lstrip().split('\n')[1:]

print(fasta_header)
print(fasta_sequence)

# Fasta concatenado
catfasta = ''

for portion in fasta_sequence:
    catfasta = catfasta + portion

print("FASTA header is:\n", fasta_header)
print("New concatenated sequence is:\n", catfasta)
------------------------------------------------------------------------------
""" 

## Real code starting NOW!

## Base UNIPROT query id
base_url = "https://www.uniprot.org/uniprot/"

# 1. Abrir lista de cabeçalhos txt
ids_fh = open(sys.argv[1], 'r')

## Procura a expressão regular
def SearchMotif(fasta, header):
    matches = []
    for match in re.finditer(r"N[^P][ST][^P]", fasta, overlapped=True):
        s = match.start()
        matches.append(s+1)
        
    # Exibe o cabeçalho e os matches
    if matches:
        print(header)
        print(*matches)
    
for entry in ids_fh:
    """ Etapa 1
    Parse HTML to get back fasta proteins
    """
    
    # Capturar o fasta
    entry = entry.rstrip()
    query_url = base_url + entry + ".fasta"
    query_html = urlopen(query_url)
    query_soup = BeautifulSoup(query_html, 'html.parser')
    query_fasta = query_soup.get_text()
    #print(entry)
    #print(query_fasta)
    
    ## Pula a primeira linha
    first_counter = 0
    seq = ""
    
    ## Captura somente a sequência
    for line in query_fasta.rsplit("\n"):
        if first_counter > 0:
            seq = seq + line
            
        first_counter = first_counter + 1
    
    # Exibe a sequência
    # print(seq.rstrip('\n'))
    
    """ The actual regex
    """
    
    # Buscar o padrão na sequência.
    SearchMotif(seq.rstrip('\n'), entry)
    

    
    




