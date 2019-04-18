# -*- coding: cp1252 -*-
#PROGRAMA 48
posicao = ' '
vetor = []
a = int(input('Digite um número: '))
while a >= 0:
    vetor.append(a)
    a = int(input('Digite um número: '))

n = int(input('Digite um valor: '))
for i in range (0,len(vetor)):
    if vetor[i] == n:
        posicao = i
if posicao == ' ':
    print 'Valor não encontrado!'
else:
    print 'Posição:', posicao
