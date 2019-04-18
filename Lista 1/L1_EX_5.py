#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 1: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 5 
p1 = input ('Insira a Nota da primeira prova (P1): ')
p2 = input ('Insira a Nota da segunda prova(P2): ')
t = input ('Insira a Nota do trabalho (T): ')
l1 = input ('Insira a Nota da primeira lista (L1): ')
l2 = input ('Insira a Nota da segunda lista (L2): ')
l3 = input ('Insira a Nota da terceira lista (L3): ')
l4 = input ('Insira a Nota da quarta lista (L4): ')
l5 = input ('Insira a Nota da quinta lista (L5): ')
mlista=(l1+l2+l3+l4+l5)/5
media=0.3*p1+0.4*p2+0.2*mlista+0.1*t
print 'A médias do aluno é: ',media
