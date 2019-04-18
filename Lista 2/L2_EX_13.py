# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 2: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 13
a = float (input ('Digite o número de eleitores: '))
b = float (input ('Digite a quantidade de votos brancos: '))
c = float (input ('Digite a quantidade de votos nulos: '))
d = float (input ('Digite a quantidade de votos válidos: '))
vb = (b/a)*100
vn = (c/a)*100
vv = (d/a)*10000
print vb, '% de votos brancos', vn, '% de votos nulos', vv, '% de votos válidos'
