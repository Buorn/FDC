# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 3: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 30
for i in range (1,10000):
    soma =0
    for j in range (1,i):
        if i%j == 0:
            soma += j
    if soma == i:
        print i
            


