# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 2: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 10
a = float (input ('Digite sua altura: '))
b = raw_input ('Digite seu sexo (M) (F) :')
m = (72.7*a)-58.0
f = (62.1*a)-44.0
if b == 'M' or b == 'Masculino' or b == 'masculino' or b == 'm':
    print 'Seu peso ideal é', m
elif b == 'F' or b == 'Feminino' or b == 'feminino' or b == 'f':
    print 'Seu peso ideal é', f
else:
    print 'Digite seu sexo corretamente'
