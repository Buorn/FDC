# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 5: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 7
def cVet(v): #CRIA VETOR
    for i in range(0,10):
        v.append(int(input('Elemento: ')))
    return v


def uniao(x,y): #ARMAZENA OS VETORES 2 VETORES EM UM S�, COME�ANDO PELO SEGUNDO VETOR
    vet=[0]*20
    for i in range(0,len(x)):
        vet[i]=y[i]
        vet[i+10]=x[i]
    return vet

v1=[]
v2=[]
print 'Vetor 1'
v1=cVet(v1)
print 'Vetor 2'
v2=cVet(v2)
print 'Vetor 1:',v1
print 'Vetor 2:',v2
print 'Vetor 3:',uniao(v1,v2)
