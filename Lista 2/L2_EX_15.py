# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 2: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 15
a = input ('Digite um n�mero entre 1000 e 9999: ')
mc = a//100
du = a%100
soma = mc + du
q = soma**2
if q == a:
    print 'Este valor obedece a seguinte caractetistica'
    print 'Valor escolhido:',a
    print 'parcela da milhar e centena:', mc
    print 'parcela da dezena e unidade:', du
    print mc, '+', du, '=', soma
    print soma, 'ao quadrado =', q
else:
    print 'Este valor n�o obedece a caracteristica'
