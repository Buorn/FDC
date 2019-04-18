# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 3: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 30
for i in range (1,10000):
    soma =0
    for j in range (1,i):
        if i%j == 0:
            soma += j
    if soma == i:
        print i
            


