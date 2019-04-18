# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 3: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 29
soma =0
i = input ('Digite um número: ')
for j in range (1,i):
    if i%j == 0:
        soma += j
if soma == i:
    print i, 'é um número perfeito.'
else:
    print i, 'não é um número perfeito.'
