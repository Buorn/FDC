# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 3: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 21
cont = 1
cont1 = 1
mm_altura = 0
m_altura = 0
a = 0
while a != 1:
    nome = raw_input ('Digite o nome: ') 
    altura = float (input ('Digite a altura: '))
    print 'Nome: ', nome, 'tem ', altura, 'metros de altura'
    if altura >= m_altura:
        if altura == m_altura:
            cont += 1
        m_altura = altura
    elif altura >= mm_altura:
        if altura == mm_altura:
            cont1 += 1
        mm_altura = altura
    if nome == 'Maria':
        a = 1
print 'A duas maiores alturas s�o: ', m_altura, ' e ', mm_altura
print cont, 'mulheres tem ', m_altura, 'e', cont1, 'mulheres tem ', mm_altura
#cont�m um bug na contagem: Caso seja digitadas alturas iguais menores que a maior, d� erro na contagem.!!!
