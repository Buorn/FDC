# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 4: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 7
a = raw_input ('Digite uma palavra: ')
b = raw_input ('Digite uma palavra: ')
for i in range (0,len(a)):
    c = b.count (a[i])
    if c >= 1:
        print a[i]
