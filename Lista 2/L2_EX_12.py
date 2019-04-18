# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 2: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 12
a = float (input ('Digite a quantidade de horas trabalhadas pelo professor 1: '))
b = float (input ('Digite o valor da hora do professor 1: '))
c = float (input ('Digite a quantidade de horas trabalhadas pelo professor 2: '))
d = float (input ('Digite o valor da hora do professor 2: '))
s1 = a*b
s2 = c*d
if s1 > s2:
    print 'O professor 1 tem o maior salário'
else:
    print 'O professor 2 tem o maior salário'
