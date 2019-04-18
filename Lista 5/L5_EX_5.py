# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 5: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 5
def cVet(v): #CRIA VETOR
    for i in range(0,5):
        v.append(int(input('Elemento: '))) 
    return v


def cVar(): #LER VARIÁVEL
    a = int(input('Valor: '))
    return a


def cont(v,x): #CONTA O NÚMERO DE VEZES QUE UM CERTO ELEMENTO
    cont=0
    for i in range(0,len(v)):
        if v[i]==x:
            cont+=1
    print 'O elemento',x,'aparece', cont,'vezes no vetor'


#PROGRAMA PRINCIPAL
v1=[]
v1=cVet(v1)
x = cVar()
cont(v1,x)
