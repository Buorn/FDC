# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 3: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 8
soma = 0
a = input ('Digite um número inteiro: ')
b = input ('Digite um número inteiro: ')
for i in range (a+1,b):
    if i%4 == 0 and a<b:
        soma += i
    elif a>b:
        print 'A soma não será realizada.'
print 'A soma dos múltiplos de 4 entre', a, 'e', b, 'é:', soma 
        
