# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 3: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 7
soma = 0
a = input ('Digite um n�mero inteiro: ')
b = input ('Digite um n�mero inteiro: ')
for i in range (a, b+1):
    if a < b:
        soma += i
    else:
        print 'A soma n�o ser� realizada. O primeiro n�mero tem que ser menor que o segundo.'
print 'A soma entre os n�meros inseridos �: ',soma
    
