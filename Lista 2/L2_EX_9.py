# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 2: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 9
a = float (input ('Digite o valor do produto:'))
a1 = a*(1+0.05)
a2 = a*(1+0.10)
a3 = a*(1+0.15)
if a <= 50:
    print 'Barato: R$',a1
elif a <= 100 and a2 <= 80:
    print 'Barato: R$',a2
elif a <= 100 and a2 <= 120:
    print 'Normal: R$',a2
elif a > 100 and a3 <= 120:
    print 'Normal: R$',a3
elif a > 100 and a3 <= 200:
    print 'Caro: R$',a3
else:
    print 'Muito Caro: R$',a3
