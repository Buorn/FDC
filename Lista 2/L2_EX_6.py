# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 2: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 6
a = input ('Digite o primeiro n�mero:')
b = input ('Digite o segundo n�mero:')
c = input ('Digite o terceiro n�mero:')
if a < b and b < c:
    print a, b, c
elif a < c and c < b:
    print a, c, b
elif b < a and a < c:
    print b, a, c
elif b < c and c < a:
    print b, c, a
elif c < a and a < b:
    print c, a, b
else:
    print c, b, a
