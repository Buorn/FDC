# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 5: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 17
def cMat(m): #CRIA MATRIZ NULA
    for i in range(0,5):
        m.append(0)
        m[i]=[]
        for j in range(0,5):
            m[i].append(0)
    return m


def pMatI(m): #IMPRIME A MATRIZ IDENTIDADE
    for i in range(0,5):
        m[i][i]=1
    print 'Matriz identidade:', m


#PROGRAMA PRINCIPAL
mat=[]
mat=cMat(mat)
print mat
pMatI(mat)
