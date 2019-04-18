# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 3: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 17
a = float( input ('Digite a medida da base do triângulo: '))
b = float( input ('Digite a medida da altura do triângulo: '))
if a <= 0 or b <= 0:
    print 'Digite valores válidos'
else:
    area = a*b/2
    print 'A área deste triângulo é: ', area
