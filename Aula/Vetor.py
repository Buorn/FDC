# -*- coding: utf-8 -*-
cont = 0
soma = 0
nota = [0.0]*5
for i in range (0,5):
    nota[i] = float(input('Digite a nota do Aluno: '))
    soma += nota[i]
media = soma/5
print 'Média da turma é: ', media
for j in range (0,5):
    if nota[j]>media:
        cont += 1
        print 'Nota maior que a média da turma:', nota[j]
print cont, 'alunos ficaram acima da média da turma'
