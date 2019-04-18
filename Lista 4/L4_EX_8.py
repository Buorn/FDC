# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 4: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 7
a = raw_input ('Digite uma palavra: ')
b = raw_input ('Digite uma palavra: ')
for i in range (0,len(a)):
    c = b.count (a[i])
    if c >= 1:
        print a[i]
