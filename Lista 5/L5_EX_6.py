# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 5: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 6
def cVet(v): #CRIA VETOR
    for i in range(0,5):
        v.append(int(input('Elemento: ')))
    return v


def par(v): #CONTA A QUANTIDADE DE ELEMENTOS PARES
    cont=0
    for i in range(0,len(v)):
        if v[i]%2==0:
            cont+=1
    print 'Quantidade de Pares:',cont

    
#PROGRAMA PRINCIPAL
vet=[]
vet=cVet(vet)
print 'Vetor:', vet
par(vet)
    
