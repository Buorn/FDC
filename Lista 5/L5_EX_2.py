# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 5: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 2
def cVar(): #LER VARIAVEL
    a=int(input('Valor: '))
    return a


def cVet(v): #CRIA VETOR
    for i in range(0,12):
        v.append(int(input('Elemento:')))
    return v


def soma(vet,x,y): #SOMA OS ELEMENTOS DOS VETORES DAS POSIÇÕES DIGITADAS
    soma=0
    for i in range(0,len(vet)):
        if x-1 == i:
            soma+=vet[i]
        if y-1 == i:
            soma+=vet[i]
    return soma


#PROGRAMA PRINCIPAL
vet=[]
vet=cVet(vet)
x = cVar() 
y = cVar()
print 'Soma:', soma(vet,x,y)
