# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 5: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 12
def lervetor(v): #CRIA VETOR
    for i in range(0,5):
        v.append(int(input('Elemento: ')))
    return v


def uniao(u,v1,v2): #UNIÃO ENTRE DOIS VETORES
    for i in range(0,5):
            u[i]=v1[i]
            u[i+5]=v2[i]
    for i in range(0,5):
        for j in range(0,5):
            if v2[i]==v1[j]:
                u.remove(v2[i])
    u.sort()
    return u

        
def inters(x,v1,v2): #INTERSECÇÃO ENTRE DOIS VETORES
    for i in range(0,5):
        for j in range(0,5):
            if v1[i]==v2[j]:
                x[i]=v1[i]          
    for k in range(0,x.count(0)):
        x.remove(0)                
    return x


#PROGRAMA PRINCIPAL
v1=[]
v2=[]
u=[0]*10
x=[0]*5
v1=lervetor(v1)
v2=lervetor(v2)
print "Vetor 1:",v1
print "Vetor 2:",v2
print "União V1 e V2:",uniao(u,v1,v2)
print "Interseção V1 e V2:",inters(x,v1,v2)

