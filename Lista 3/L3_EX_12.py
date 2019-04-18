# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 3: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 12
cont = 0
med_t = 0
for j in range (0, 2):
    nome_t = raw_input ('Digite o nome da turma: ')
    for i in range (0, 5):
        nome_a = raw_input ('Digite o nome do aluno: ')
        nota1 = float (input ('Digite a primeira nota do aluno: '))
        nota2 = float (input ('Digite a segunda nota do aluno: '))
        med_a = (nota1 + nota2)/2
        if med_a >= 7:
            print 'Aluno aprovado!'
        elif med_a >= 4:
            print 'Aluno em exame final!'
        else:
            print 'Aluno reprovado!'
        med_t += med_a
        cont += 1
        med = med_t/cont
    print 'Média da turma', nome_t, 'é: ',med
