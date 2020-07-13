#!/usr/bin/env python

"""
-----
Prob 13: Lia

Given k generations, the P(%) that they'll have at least N
offspring whose genotype is AaBb.

All mates are AaBb.
The starting parent is Tom, which is AaBb.
---
rcs.biotec@gmail.com
"""

## Read the file
import sys
import math

## Inputs
input_fh = open(sys.argv[1], 'r')
k, n = input_fh.read().split(' ')

k = int(k)
n = int(n)

## Still breaks!
# k = 3
# n = 5

# Todas as gerações
# print("generations (K) are: ", k)

# Todos os sucessos
# print("successes (N) are: ", n)

# Número de filhotes
t = 2 ** int(k)
# print("total offspring (t) are: ", t)

# Chance de sucesso
p = 0.25
# print("Prob of success is: ", p)

# Define a função fatorial
def Comb(a, b):
    fact = math.factorial
    out = (fact(a) / (fact(b) * (fact(a-b))))
    return(out)
 
# Calcula para uma geração
def probCalc(k, n, p):
    me = k
    ma = n
    prob = Comb(ma, me) * (p ** me) * ((1 - p) ** (ma - me))
    return(prob)
    
## Guarda o valor final    
prob_f = 0

# Calcula para cada geração o número de indivíduos positivos
if n == 1:
    for value in range(1, t+1):
        prob_f = prob_f + probCalc(value, t, p)
        # print(prob_f)
else:
    for value in range(n, t+1):
        prob_f = prob_f + probCalc(value, t, p)
        # print(value, '\t', probCalc(value, t, p), '\t', prob_f)
    
    
# Exibe a prob. final    
print(round(prob_f, 5))

# print(probCalc(n, t, p))
# print(probCalc(n+1, t, p))
# print(probCalc(n+2, t, p))
# print(probCalc(n+3, t, p))


