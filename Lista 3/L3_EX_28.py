# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 3: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 27
n = input ('Digite um n�mero: ')
for j in range (1, n+1):
    cont = 0
    for i in range (1,j+1):
        a = j%i
        if a == 0:
            cont += 1
    if cont == 2:
        print j
