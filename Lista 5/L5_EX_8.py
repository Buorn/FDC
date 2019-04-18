# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 5: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 8
def cVet(v): #CRIA VETOR
    for i in range(0,15):
        v.append(int(input('Elemento: ')))
    return v


def soma(v1,v2): #SOMA OS ELEMENTOS DE DOIS VETORES
    vs=[0]*len(v1)
    for i in range(0,len(v1)):
        vs[i]=v1[i]+v2[i]
    print 'Vetor soma:',vs

def dif(v1,v2): #SUBTRAÇÃO COM ELEMENTOS DE DOIS VETORES
    vd=[0]*len(v1)
    for i in range(0,len(v1)):
        vd[i]=v1[i]-v2[i]
    print 'Vetor diferença:',vd


#PROGRAMA PRINCIPAL
v1=[]
v2=[]
print 'Vetor 1'
v1=cVet(v1)
print 'Vetor 2'
v2=cVet(v2)
print 'Vetor 1:',v1
print 'Vetor 2:',v2
soma(v1,v2)
dif(v1,v2)
