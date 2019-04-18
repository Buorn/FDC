# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 3: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 9
soma = 0
b = float (input ('Digite o comprimento do comodo: '))
while b > 0:
    h = float (input ('Digite o largura do comodo: '))
    a = b*h
    soma += a
    b = float (input ('Digite o comprimento do comodo: '))
print 'Área total: ', soma
