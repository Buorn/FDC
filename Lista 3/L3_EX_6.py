# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 3: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 6
soma = 0
for i in range (1,51):
    qtd = input ('Digite a quantidade do produto: ')
    vu = float (input ('Digite o pre�o do produto: '))
    vt = qtd*vu
    soma += vt
print 'O valot total �:', soma
