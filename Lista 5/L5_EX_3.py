# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 5: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 3
def cVet(v): #CRIA VETOR
    for i in range(0,6):
       v.append(int(input('Elemento: ')))
    return v


def troca(v1): #TROCA A POSI��O DA PRIMEIRA METADE DOS VALORES COM A SEGUNDA METADE
    v2=[0]*len(v1)
    for i in range(0,6):
        if i<3:
            v2[i+3]=v1[i]
        if i>=3:
            v2[i-3]=v1[i]
    return v2


#PROGRAMA PRINCIPAL
v1=[]
v1=cVet(v1)
print 'Vetor 1:',v1
print 'Vetor 2:',troca(v1)
