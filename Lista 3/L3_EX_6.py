# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 3: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 6
soma = 0
for i in range (1,51):
    qtd = input ('Digite a quantidade do produto: ')
    vu = float (input ('Digite o preço do produto: '))
    vt = qtd*vu
    soma += vt
print 'O valot total é:', soma
