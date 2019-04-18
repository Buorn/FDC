# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 2: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 19
a = input ('Digite a hora de sua partida: ')
b = input ('Digite os minutos de sua partida: ')
c = input ('Digite os segundos de sua partida: ')
d = input ('Digite a hora de sua chegada: ')
e = input ('Digite os minutos de sua chegada: ')
f = input ('Digite os segundos de sua chegada: ')
si = a*3600 + b*60 + c
sf = d*3600 + e*60 + f
dt = sf - si
h = dt//3600
m = (dt%3600)//60
s = (dt%3600)%60
print 'O tempo total de viagem foi de:', h, ':', m, ':', s
