# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 5: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 13
def lervetor(v):
    for i in range(0,5):
        v.append(float(input('Temperatura em Celcius: ')))
    return v


def far(u,v): #CONVERTE GAUS CELSIUS EM FIRENHEITS EM VETOR
    for i in range(0,5):
        u[i]=(v[i]*(9.0/5))+32
    return u


def mediaf(u): #C�LCULA A M�DIA DOS ELEMENTOS DO VETOR
    su=0
    for i in range(0,5):
        su+=u[i]
    mu=su/5
    return mu


def mediac(v): #C�LCULA A M�DIA DOS ELEMENTOS DO VETOR
    sv=0
    for i in range(0,5):
        sv+=v[i]
    mv=sv/5
    return mv


def qtdf(u): #C�LCULA QUANTIDADE DE VALORES ACIMA DA M�DIA
    cont=0
    for i in range(0,5):
        if u[i]>mediaf(u1):
            cont+=1
    return cont


def qtdc(v): #C�LCULA QUANTIDADE DE VALORES ACIMA DA M�DIA
    cont1=0
    for i in range(0,5):
        if v[i]>mediac(v1):
            cont1+=1
    return cont1


#PROGRAMA PRINCIPAL
v1=[]
u1=[0.0]*5
v1=lervetor(v1)
u1=far(u1,v1)
medf=mediaf(u1)
medc=mediac(v1)
print 'Gruas Celsius:',v1
print 'Graus Firenheit:',u1
print 'M�dia Graus Firenheit:',medf
print 'M�dia Graus Celsius:',medc
print 'Graus Firenheit acima da m�dia:',qtdf(u1)
print 'Graus Celsius acima da m�dia:',qtdc(v1)
