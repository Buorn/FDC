# -*- coding: utf-8 -*-
#PROGRAMA 50_solução professor
vet1 = []
num = int(input('Num: '))
while num >=0:
    vet1.append(num)
    num = int(input('Num: '))


Vet2 = [0]*len(vet1)
for i in range (0,len(vet1)):
    if i%2 == 0:
        vet2[i] = vet1[i]*2
    else:
        vet2[i] = vet1[i]*3-1
