# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 3: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 24
cont = 0
cont1 = 0
cont2 = 0
n = input ('Digite o n�mero de crian�as nascida: ')
sexo = raw_input ('Digite o sexo da crian�a morta, "m" para masculino e "f" para feminino: ')
while sexo.lower() != 'vazio':
    meses = input ('Digite o n�mero de meses que a crian�a viveu: ')
    cont += 1.0
    if sexo.lower() == 'm':
        cont1 += 1.0        
    if meses <= 24:
        cont2 += 1.0
    sexo = raw_input ('Digite o sexo da crian�a morta, "m" para masculino e "f" para feminino: ')
perc_morte = (cont/n)*100
perc_masc = (cont1/cont)*100
perc_24m = (cont2/cont)*100
print 'Crian�as mortas: ', perc_morte, '%'
print 'Crian�as mortas do sexo masculino: ', perc_masc, '%'
print 'Crian�as que viveram at� 24 meses: ', perc_24m, '%'
