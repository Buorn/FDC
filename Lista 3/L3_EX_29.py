# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 3: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 29
soma =0
i = input ('Digite um n�mero: ')
for j in range (1,i):
    if i%j == 0:
        soma += j
if soma == i:
    print i, '� um n�mero perfeito.'
else:
    print i, 'n�o � um n�mero perfeito.'
