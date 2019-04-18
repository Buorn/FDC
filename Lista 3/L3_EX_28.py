# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 3: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 27
n = input ('Digite um número: ')
for j in range (1, n+1):
    cont = 0
    for i in range (1,j+1):
        a = j%i
        if a == 0:
            cont += 1
    if cont == 2:
        print j
