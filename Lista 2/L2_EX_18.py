# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 2: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 18
a = float (input ('Digite seu saldo banc�rio: '))
if a < 100:
    print 'Isento'
elif a < 1000:
    print 'Imposto devido � 1% sobre o saldo'
elif a < 10000:
    print 'Imposto devido � 2% sobre o saldo'
elif a < 100000:
    print 'Imposto devido � 3% sobre o saldo'
else:
    print 'Imposto devido � 5% sobre o saldo'
