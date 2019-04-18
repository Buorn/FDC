#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#FUNDAMENTOS DA COMPUTAÇÃO
#BRUNO BANDEIRA BRANDÃO
#AULA 2: PYTHON
#EXERCÍCIO 1
a = float (input ('Digite a primeira nota:'))
b = float (input ('Digite a segunda nota:'))
m = (a + b)/2
if m >= 7:
    print 'Aluno está Aprovado com média', m
else:
    if m >= 4:
        print 'Aluno está em Prova final com média',m
    else:
        print 'Aluno está Reprovado com média',m
