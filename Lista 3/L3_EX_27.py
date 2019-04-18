# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 3: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 27
cont = 0
n = input ('Digite um número: ')
for i in range (1,n+1):
    a = n%i
    if a == 0:
        cont += 1
if cont == 2:
    print n, 'é um número primo.'
else:
    print n, 'não é um número primo'
