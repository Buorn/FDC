# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 3: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 10
joao = 0
jose = 0
maria = 0
branco = 0
nulo = 0
for i in range (0,20000):
    voto = input ('Digite o número do seu candidato: ')
    if voto == 1:
        joao += 1
    elif voto == 2:
        jose += 1
    elif voto == 3:
        maria += 1
    elif voto == 4:
        branco += 1
    else:
        nulo += 1
if joao > jose and joao > maria:
    print 'João da Silva recebeu mais votos'
elif  jose > maria:
    print 'Jose Ramalho da Silva recebeu mais votos'
else:
    print 'Maria Mattos recebeu mais votos'    
print 'João da Silva recebeu: ', joao, 'votos'
print 'Jose Ramalho recebeu: ', jose, 'votos'
print 'Maria Mattos recebeu: ', maria, 'votos'
print 'Votos em branco: ', branco
print 'Votos nulos: ', nulo
