# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 5: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 18
def cMat(m): #CRIA MATRIZ NULA
    for i in range(0,6):
        m.append(0)
        m[i]=[]
        for j in range(0,6):
            m[i].append(int(input('Elemento: ')))
    return m


def maior(m):
    cont=0
    for i in range(0,6):
        for j in range(0,6):
            if m[i][j]>10:
                cont+=1
    print 'Elementos maiores que 10:',cont


#PROGRAMA PRINCIPAL
mat=[]
mat=cMat(mat)
print 'Matriz:',mat
maior(mat)

