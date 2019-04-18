# -*- coding: cp1252 -*-
cont = 0
smed = 0
nome = raw_input ('Digite o nome do aluno: ')
while nome != 'FIM':
    sexo = raw_input ('Digite o sexo do aluno (M) ou (F): ')
    n1 = float (input ('Digite a primeira nota do aluno: '))
    n2 = float (input ('Digite a segunda nota do aluno: '))
    if sexo == 'F':
        print nome, ':', (n1 + n2)/2
    else:
        med = (n1 + n2)/2
        smed = smed + med
        cont = cont + 1
    nome = raw_input ('Digite o nome do aluno: ')
media = smed/cont
print 'A média dos homens é:', media
