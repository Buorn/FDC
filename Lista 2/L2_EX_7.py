# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 2: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 7
a = float (input ('Digite o primeiro n�mero:'))
b = float (input ('Digite o segundo n�mero:'))
c = raw_input ('Digite a opera��o (+),(-),(*) ou (/):')
soma = a + b
sub = a - b
m = a*b
d = a/b
if c == '+':
    print a, '+', b, '=', soma
elif c == '-':
    print a, '-', b, '=', sub
elif c == '*':
    print a, '*', b, '=', m
elif c == '/':
    print a, '/', b, '=', d
