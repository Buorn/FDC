# -*- coding: cp1252 -*-
#PROGRAMA 47
vetor = [0.0]*10
soma = 0
for i in range (0,len(vetor)):
    vetor[i] = int(input('Digite um Valor: '))
    if vetor[i]%2 == 0:
        soma+=vetor[i]
    if i%2 != 0:
        soma-=vetor[i]
print soma
