# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 3: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 3
cont1 = 0
cont2 = 0
soma = 0
a = input ('Digite um número inteiro: ')
while a != 0:
    if a%2 == 0:
        soma += a
        cont1 += 1
    else:
        cont2 += 1
    a = input ('Digite um número inteiro: ')
med = soma/float(cont1)
print 'Pares:',cont1, 'Impares:', cont2, 'Média dos pares:',med 
