# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 4: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 6
b = ' '
a = raw_input ('Digite uma palavra: ')
for i in range (0, len(a)):
    if a[i] == 'a' or a[i] == 'e' or a[i] == 'i' or a[i] == 'o' or a[i] == 'u': 
        b += a[i]*2
    else:
        b += a[i]
print b
