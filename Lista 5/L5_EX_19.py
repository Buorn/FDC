# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 5: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 19
def cMat(m): #CRIA MATRIZ
    for i in range(0,4):
        m.append(0)
        m[i]=[]
        for j in range(0,4):
            m[i].append(int(input('Elemento: ')))
    return m


def cVar(): #LER VARIÁVEL
    s=int(input('Valor: '))
    return s


def procura(m,s): #PROCURA O VALOR ESCOLHIDO E IMPRIME SUA LINHA E COLUNA
    cont=0
    for i in range(0,4):
        for j in range(0,4):
            if m[i][j]==s:            
                
            else:
                cont+=1
    if cont==16:
        print 'Valor não encontrado!'

    print 'Linha:',v1[0]
    print 'Coluna:',v2[0]
#PROGRAMA PRINCIPAL
mat=[]
mat=cMat(mat)
x=cVar()
procura(mat,x)
