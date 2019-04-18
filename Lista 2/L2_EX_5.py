# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 2: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 5
a = float (input ('Digite a primeira nota:'))
b = float (input ('Digite a segunda nota:'))
c = float (input ('Digite a terceira nota:'))
m = (a + b + c)/3
dif = (12 - m)
if m >= 7:
    print 'Aluno Aprovado'
elif m >= 4:
    print 'Aluno em exame. Precisa de', dif, 'para ser aprovado'
else:
    print 'Aluno reprovado'
