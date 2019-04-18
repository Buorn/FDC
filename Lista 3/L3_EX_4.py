# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 3: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 4
maior = 0
nmaior = ' '
nome = raw_input ('Digite o nome do produto: ')
while nome != 'xxx':
    preco = float(input('Digite o valor do produto: '))
    if maior < preco:
        maior = preco
        nmaior = nome
    nome = raw_input ('Digite o nome do produto: ')   
print 'O produto mais caro é:', nmaior, 'e custa R$', maior 
