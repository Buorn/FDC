# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 5: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 16
def cMat(m): #CRIA MATRIZ
    for i in range(0,7):
        m.append(0)
        m[i]=[]
        for j in range(0,7):
            m[i].append(int(input('Elemento: ')))
    return m


def lin6(m): #SOMA DOS ELEMENTOS DA LINHA 6
    soma=0
    for i in range(0,7):
        soma+=m[6][i]
    print 'Soma da linha 6:',soma
            

def col2(m): #SOMA DOS ELEMENTOS DA COLUNA 2
    soma=0
    for i in range(0,7):
        soma+=m[i][2]
    print 'Soma da coluna 2:',soma
    

def digpri(m): #SOMA DOS ELEMENTOS DA DIAGONAL PRINCIPAL
    soma=0
    for i in range(0,7):
        soma+=m[i][i]
    print 'Soma da Diagonal principal:',soma


def l3c4(m): #IMPRIME O ELEMENTO DA LINHA 3 COLUNA 4
    print 'Elemento da linha 3, Coluna 4:',m[3][4]


def par(m): #SOMA DOS ELEMENTOS PARES DA MATRIZ
    soma=0
    for i in range(0,7):
        for j in range(0,7):
            if m[i][j]%2==0:
                soma+=m[i][j]
    print 'Soma dos Elemmentos pares:',soma


#PROGRAMA PRINCIPAL
mat=[]
mat=cMat(mat)
print mat
lin6(mat)
col2(mat)
digpri(mat)
l3c4(mat)
par(mat)

