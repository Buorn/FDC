#PROGRAMA 41
nome = raw_input ('Digite uma palavra: ')
soma = 0
for i in range (0,len(nome)):
    letra = nome[i]
    soma += ord(letra)
print 'Soma: ', soma
