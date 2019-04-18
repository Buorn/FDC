nome = raw_input ('Digite um nome: ')
soma = 0
for i in range (0,len(nome)):
    letra = nome[i].lower()
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        soma += 1
print ' Quantidade de vogal: ', soma
