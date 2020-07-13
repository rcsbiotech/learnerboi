#!/usr/bin/env python

# Necessário para importar arquivos
import sys

# Capturar o arquivo
data_fh = open(sys.argv[1], 'r')

# Captura a string da primeira linha
intel = data_fh.readline()

# Remove newline
intel = str(intel.rstrip('\n'))

# Separa os elementos
split_intel = intel.split(' ')

# Cria uma variável cada
# N - var_months
# k - var_litter
var_months = int(split_intel[0])
var_litter = int(split_intel[1])

# AT
print("Months to cycle: ", var_months)
print("Rabbits per litter: ", var_litter)
print('\n')

## Explicit variables
cur_month = 1

## Starting values

# 3 processos: M, bi e repx

## Passa do mês 1 (cur_moth) até o último (var_months+1)
while cur_month < var_months+1:

        # Sempre são 02 no primeiro e segundo mês
	if (cur_month == 1 or cur_month == 2):
		NR = 1
		NRPM = 1
		NRPP = 1
	else:
                # [.. A partir do terceiro mês ..] #
                # NR - total de pares
                # NRPM - pares "amadurecidos" não se reproduzem
                # MRPP - pares que reproduziram mês passado
		NR = NRPM + (var_litter * NRPP)
				
	print("Atualizando o mês...\n\n")
	# Atualiza o mês
	cur_month = cur_month + 1
	print("Mês atual: ", cur_month)
	print("NR: ", NR)
        # -- cálculos do próximo mês!

        # Atualiza as variáveis:
        ## número de coelhos que vão se reproduzir (NRPP)
        ## é igual ao número de coelhos amadurecidos até o mês passado (NRPM)
	NRPP = NRPM

        ## O número de colehos que nasceram é o total calculado acima (NR)
	NRPM = NR

