# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 3: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 23
cont = 0
cont1 = 0
cont2 = 0.0
for i in range (0,5):
    sexo = raw_input ('Digite o sexo do entrevistado, "m" para masculino e "f" para feminino: ')
    r = raw_input ('Digite a resposta, "s" para sim e "n" para n�o:')
    if r.lower() == 's':
        cont += 1
    else:
        cont1 += 1
    if sexo == 'm' and r == 'n':
        cont2 += 1
perc = (cont2/(cont + cont1))*100
print cont, 'pesoas responderam sim e', cont1, 'pessoas responderam n�o.'
print perc, '% dos homens responderam n�o.'
