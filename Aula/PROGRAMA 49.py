# -*- coding: utf-8 -*-
#PROGRAMA 49
vetor1 = [0.0]*5
vetor2 = [0.0]*5
for i in range (0,5):
   vetor1[i] = input('Digite valor para o Vetor 1: ')
for i in range (0,5):
   vetor2[i] = input('Digite valor para o Vetor 2: ')

print 'Vetor 1: ',vetor1
print 'Vetor 2: ',vetor2


for i in range (0,5):
    for j in range (0,5):
        if vetor1[i]==vetor2[j]:
            print 'Interseção: ',vetor1[i]
