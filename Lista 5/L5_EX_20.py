# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 5: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 20
def cMat(m): #CRIA MATRIZ
    for i in range(0,4):
        m.append(0)
        m[i]=[]
        for j in range(0,4):
            m[i].append(int(input('Elemento: ')))
    return m


def troca(m1,m2): #TROCA LINHA 2 COM COLUNA 4
    
    
