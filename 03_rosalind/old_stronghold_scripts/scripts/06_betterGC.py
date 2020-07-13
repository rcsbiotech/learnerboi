#!/usr/bin/env python

def fastaread(filehandle):

    # Some arrays
    fastaid = []
    seqarray = []

    # Open file
    f = openandread(handle)

    # Passa todos os espaços em branco
    while True:
        line = f.readline

        if line is empty:
            return
        if line[0] is '>':
            break

    while True:
        # Se não tiver '>', quebra
        if not line.startswith('>'):
            raise Error(
                    "FASTA records start with '>'")

        # Se estiver tudo certo, continua
        title = line[1:end].rstrip()
        fastaid.append(title)

        # Para guardar a sequência
        seqdata = []
        line = f.readline()

        # Extrai a sequência
        while True:
            if not line:
                break
            if line [0] == '>':
                break
            seqdata.append(line.rstrip())
            line = f.readline()

        # Guarda os nucleotídeos
        nts = ''.join(seqdata).replace(" ", "").replace("\r", "")
        seqarray.append(nts)

        if not line:
            return fastaid, seqarray

def percentgc(fastaids, seqarray):

    seqgc = [];

    if len(fastaids) != len(seqarray):
        return ValueError(
                "The number of records and sequences isnt the same")

    for seq in seqarray:
        gccount = seq.count('G') + seq.count('C')
        totcount = len(seq)
        seqgc.append(100*gccount/totcount)

    max_gc = max(seqgc)
    max_index = seqgc.index(max_gc)

    print fastaids[max_index]
    print max_gc
