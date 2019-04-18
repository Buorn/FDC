# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 3: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 21
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
print 'A duas maiores alturas são: ', m_altura, ' e ', mm_altura
print cont, 'mulheres tem ', m_altura, 'e', cont1, 'mulheres tem ', mm_altura
#contém um bug na contagem: Caso seja digitadas alturas iguais menores que a maior, dá erro na contagem.!!!
