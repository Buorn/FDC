# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 3: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 9
soma = 0
b = float (input ('Digite o comprimento do comodo: '))
while b > 0:
    h = float (input ('Digite o largura do comodo: '))
    a = b*h
    soma += a
    b = float (input ('Digite o comprimento do comodo: '))
print '�rea total: ', soma
