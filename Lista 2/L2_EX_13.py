# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 2: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 13
a = float (input ('Digite o n�mero de eleitores: '))
b = float (input ('Digite a quantidade de votos brancos: '))
c = float (input ('Digite a quantidade de votos nulos: '))
d = float (input ('Digite a quantidade de votos v�lidos: '))
vb = (b/a)*100
vn = (c/a)*100
vv = (d/a)*10000
print vb, '% de votos brancos', vn, '% de votos nulos', vv, '% de votos v�lidos'
