# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 3: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 18
cont = 0.0
cont1 = 0.0
soma = 0
idade = input ('Digite sua idade: ')
while idade < 100:
    idade = input ('Digite sua idade: ')
    soma += idade
    cont += 1
    if idade >= 21 and idade <= 65:
        cont1 += 1
med = soma/cont
perc = (cont1/(cont +cont1))*100
print 'A idade m�dia dos indiv�duos � de: ', med
print 'Percentual de pessoas entre 21 e 65 � de: ', perc, '%'
