# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 3: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 8
soma = 0
a = input ('Digite um n�mero inteiro: ')
b = input ('Digite um n�mero inteiro: ')
for i in range (a+1,b):
    if i%4 == 0 and a<b:
        soma += i
    elif a>b:
        print 'A soma n�o ser� realizada.'
print 'A soma dos m�ltiplos de 4 entre', a, 'e', b, '�:', soma 
        
