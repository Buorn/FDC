# -*- coding: utf-8 -*-
#PROGRAMA 50
vetor1 = [0.0]*5
vetor2 = [0.0]*5
for i in range (0,5):
   vetor1[i] = input('Digite valor para o Vetor 1: ')


   
for i in range (0,5):
    if i%2 == 0:
        vetor2[i] = vetor1[i]*2
    else:
        vetor2[i] = (vetor1[i]*3)-1

print 'Vetor 1: ',vetor1
print 'Vetor 2: ',vetor2
