# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 3: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 19
p = 0.0
p2 = 100000.0
for i in range (1, 5):
    num = raw_input ('Digite o número do boi: ')
    peso = float (input ('Digite o peso do boi: '))
    if p < peso:
        p = peso
        n = num
    if p2 > peso:
        p2 = peso
        n2 = num
print 'O boi', n, 'é o mais gordo, pesando', p, 'kg'
print 'O boi', n2, 'é o mais magro, pesando', p2, 'kg'
