# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 3: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 2
a = input ('Digite o primeiro termo da PA:')
r = input ('Digite a razao da PA:')
for i in range (1, 15):
    an = a +( i - 1)*r    
    print 'termo',i, ':', an
