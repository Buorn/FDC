# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 3: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 32
saque = input ('Digite o valor a ser sacado: ')
while saque != 0:
    nota_50 = saque//50
    nota_20 = (saque%50)//20
    nota_10 = ((saque%50)%20)//10
    nota_5 = (((saque%50)%20)%10)//5
    nota_1 = (((saque%50)%20)%10)%5
    total = nota_50 + nota_20 + nota_10 + nota_5 + nota_1
    print 'Total de notas: ', total
    if nota_50 !=0:
        print nota_50, 'notas de R$50.' 
    if nota_20 !=0:
        print nota_20, 'notas de R$20.'
    if nota_10 !=0:
        print nota_10, 'notas de R$10.'
    if nota_5 !=0:
        print nota_5, 'notas de R$5.'
    if nota_1 !=0:
        print nota_1, 'notas de R$1.'
    saque = input ('Digite o valor a ser sacado: ')
