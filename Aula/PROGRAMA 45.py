# -*- coding: cp1252 -*-
#PROGRAMA 45
vetor = [0.0]*4
cont = 0
soma = 0
contmed = 0
for i in range (0,len(vetor)):
    vetor[i] = float(input('Digite a nota do aluno: '))
    soma+=vetor[i]
    cont+=1
med = soma/cont

for i in range (0,len(vetor)):
    if vetor[i] >= med:
        contmed+=1
print 'Média da Turma:', med
print contmed, 'alunos estão acima da média.'        
