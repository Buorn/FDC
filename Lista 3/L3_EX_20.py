# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 3: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 20
m_idade = 0
cont = 0.0
cont1 = 0.0
idade = input ('Digite a idade: ')
while idade != -1:
    sexo = raw_input ('Digite o sexo masculino(M) ou feminino (F): ')
    cor_olho = raw_input ('Digite a cor dos olhos: ')
    cor_cabelo = raw_input ('Digite a cor dos cabelos: ')
    cont += 1
    if m_idade < idade:
        m_idade = idade
    if sexo.lower() == 'f' and idade < 35 and idade >18 and cor_olho.lower () == 'verdes' and cor_cabelo.lower() == 'louros':
        cont1 +=1
    idade = input ('Digite a idade: ')
porc = (cont1/cont)*100
print cont
print 'O habitante com a maior idade tem ', m_idade
print porc, '% são mulhres entre 18 e 35 anos com olhos verdes e cabelos louros'
