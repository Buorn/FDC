# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 4: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 6
b = ' '
a = raw_input ('Digite uma palavra: ')
for i in range (0, len(a)):
    if a[i] == 'a' or a[i] == 'e' or a[i] == 'i' or a[i] == 'o' or a[i] == 'u': 
        b += a[i]*2
    else:
        b += a[i]
print b
