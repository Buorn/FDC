# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 2: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 7
a = float (input ('Digite o primeiro número:'))
b = float (input ('Digite o segundo número:'))
c = raw_input ('Digite a operação (+),(-),(*) ou (/):')
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
