# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 3: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 17
a = float( input ('Digite a medida da base do tri�ngulo: '))
b = float( input ('Digite a medida da altura do tri�ngulo: '))
if a <= 0 or b <= 0:
    print 'Digite valores v�lidos'
else:
    area = a*b/2
    print 'A �rea deste tri�ngulo �: ', area
