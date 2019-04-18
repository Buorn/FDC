# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 5: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 11
def trajeto(v,ax): 
    for i in range(0,9):
        if i<1:
            ax[i]=v[i]
        else:
            a=(ax[i-1]-1)
            ax[i]=vet[a]
    print 'Trajetória correta:',aux


#PROGRAMA PRINCIPAL
vet=[5,7,6,9,2,8,4,0,3]
aux=[0]*9
print 'Trajetória:',vet
trajeto(vet,aux)
