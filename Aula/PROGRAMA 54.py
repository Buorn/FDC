# -*- coding: cp1252 -*-
#PROGRAMA 54
mat=[]
for i in range(0,3):
    mat.append(0)
    mat[i]=[]
    soma=0
    for j in range(0,3):
        mat[i].append(input('Elemennto: '))
        soma+=mat[i][j]
    print 'Soma da linha', i,'é: ', soma
soma2=0
for i in range(0,3):
    for j in range(0,3):
        if mat[i][j]%2 == 0:
            soma2+=mat[i][j]
print 'Soma dos elementos pares: ', soma2
