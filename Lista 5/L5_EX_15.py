# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 5: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 15
def cMat(m): #CRIA MATRIZ
    for i in range(0,5):
        m.append(0)
        m[i]=[]
        for j in range(0,5):
            m[i].append(int(input('Elemento: ')))
    return m


def maior(m): #IMPRIME O MAIOR ELEMENTO DA MATRIZ E SUA LINHA E COLUNA
    maior=0
    for i in range(0,5):
        for j in range(0,5):
            if m[i][j]>maior:
                maior=m[i][j]
                lin=i
                col=j
    print 'Maior valor:',maior
    print 'Linha:',lin
    print 'Coluna:',col
                        

#PROGRAMA PRINCIPAL
mat=[]
mat=cMat(mat)
maior(mat)
