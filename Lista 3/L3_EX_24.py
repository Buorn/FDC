# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 3: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 24
cont = 0
cont1 = 0
cont2 = 0
n = input ('Digite o número de crianças nascida: ')
sexo = raw_input ('Digite o sexo da criança morta, "m" para masculino e "f" para feminino: ')
while sexo.lower() != 'vazio':
    meses = input ('Digite o número de meses que a criança viveu: ')
    cont += 1.0
    if sexo.lower() == 'm':
        cont1 += 1.0        
    if meses <= 24:
        cont2 += 1.0
    sexo = raw_input ('Digite o sexo da criança morta, "m" para masculino e "f" para feminino: ')
perc_morte = (cont/n)*100
perc_masc = (cont1/cont)*100
perc_24m = (cont2/cont)*100
print 'Crianças mortas: ', perc_morte, '%'
print 'Crianças mortas do sexo masculino: ', perc_masc, '%'
print 'Crianças que viveram até 24 meses: ', perc_24m, '%'
