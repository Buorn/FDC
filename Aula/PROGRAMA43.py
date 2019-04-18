# -*- coding: utf-8 -*-
#PROGRAMA 43
nome = raw_input ('Digite uma palavra qualquer: ')
soma = 0
cont = 0
cont2 = 0
for i in range (0,len(nome)):
    letra = nome[i]
    if letra.isdigit() == True: #não precisava comparar com true :)
        soma += 1
    elif letra.isalpha() == True:
        cont += 1
    else:
        cont2 += 1
print'Total de números:',soma, 'total de letras:', cont, 'outros:',cont2
