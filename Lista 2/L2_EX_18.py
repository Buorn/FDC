# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 2: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 18
a = float (input ('Digite seu saldo bancário: '))
if a < 100:
    print 'Isento'
elif a < 1000:
    print 'Imposto devido é 1% sobre o saldo'
elif a < 10000:
    print 'Imposto devido é 2% sobre o saldo'
elif a < 100000:
    print 'Imposto devido é 3% sobre o saldo'
else:
    print 'Imposto devido é 5% sobre o saldo'
