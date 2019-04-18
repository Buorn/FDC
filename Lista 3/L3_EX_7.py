# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 3: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 7
soma = 0
a = input ('Digite um número inteiro: ')
b = input ('Digite um número inteiro: ')
for i in range (a, b+1):
    if a < b:
        soma += i
    else:
        print 'A soma não será realizada. O primeiro número tem que ser menor que o segundo.'
print 'A soma entre os números inseridos é: ',soma
    
