#!/usr/bin/env python

# Necessário para importar arquivos
import sys

# Capturar o arquivo
pop_fh = open(sys.argv[1], 'r')

# Captura a string da primeira linha
population = pop_fh.readline()

# Remove newline
population = str(population.rstrip('\n'))

# Separa os elementos
split_pop = population.split(' ')

# Cria uma variável cada
pop_HD = split_pop[0]
pop_HT = split_pop[1]
pop_HR = split_pop[2]

# Espaço amostral: soma das populações
sampleSpace = int(pop_HD) + int(pop_HT) + int(pop_HR)
#print(sampleSpace)

# Participação de cada população no sampleSpace
part_HD_sS = int(pop_HD)/sampleSpace
part_HT_sS = int(pop_HT)/sampleSpace
part_HR_sS = int(pop_HR)/sampleSpace

# Probabilidade menos um indivíduo
pMo_HD_sS = (int(pop_HD)-1)/(sampleSpace - 1)
pMo_HT_sS = (int(pop_HT)-1)/(sampleSpace - 1)
pMo_HR_sS = (int(pop_HR)-1)/(sampleSpace - 1)

# Probabilidade menos um de outra categoria
pPo_HD_sS = int(pop_HD)/(sampleSpace - 1)
pPo_HT_sS = int(pop_HT)/(sampleSpace - 1)
pPo_HR_sS = int(pop_HR)/(sampleSpace - 1)

# Probabilidades para cada cruzamento
## partindo de k (HD)
pR_HD_HD = part_HD_sS * pMo_HD_sS
pR_HD_HT = part_HD_sS * pPo_HT_sS
pR_HD_HR = part_HD_sS * pPo_HR_sS

## partindo de m (HT)
pR_HT_HD = part_HT_sS * pPo_HD_sS
pR_HT_HT = 0.75 * (part_HT_sS * pMo_HT_sS)
pR_HT_HR = 0.50 * (part_HT_sS * pPo_HR_sS)

## partindo de n (HR)
pR_HR_HD = part_HR_sS * pPo_HD_sS
pR_HR_HT = 0.5 * (part_HR_sS * pPo_HT_sS)
pR_HR_HR = 0.0 * (part_HR_sS * pMo_HR_sS)

print("HD x HD: ", pR_HD_HD)
print("HD x HT: ", pR_HD_HT)
print("HD x HR: ", pR_HD_HR)

print("HT x HD: ", pR_HT_HD)
print("HT x HT: ", pR_HT_HT)
print("HT x HR: ", pR_HT_HR)

print("HR x HD: ", pR_HR_HD)
print("HR x HT: ", pR_HR_HT)
print("HR x HR: ", pR_HR_HR)

# Soma das probabilidades: o dominante
sumPerc = pR_HD_HD + pR_HD_HT + pR_HD_HR + pR_HT_HD + pR_HT_HT + pR_HT_HR + pR_HR_HD + pR_HR_HT + pR_HR_HR

# Exibe a porcentagem
print(sumPerc)
