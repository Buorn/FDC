# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 5: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 11
def trajeto(v,ax): 
    for i in range(0,9):
        if i<1:
            ax[i]=v[i]
        else:
            a=(ax[i-1]-1)
            ax[i]=vet[a]
    print 'Trajet�ria correta:',aux


#PROGRAMA PRINCIPAL
vet=[5,7,6,9,2,8,4,0,3]
aux=[0]*9
print 'Trajet�ria:',vet
trajeto(vet,aux)
