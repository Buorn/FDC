# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 4: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 3
cont = 0
a = raw_input ('Digite uma palavra: ')
b = raw_input ('Digite um caractere desta palavra: ')
for i in range (0, len(a)):
    if a[i] == b:
        cont +=1
print 'A palavra', a, 'possui', cont, 'letra(s)', b
