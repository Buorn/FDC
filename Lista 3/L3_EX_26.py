# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 3: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 26
contf = 0
contm = 0
somai = 0
conti = 0
contm45 = 0
contf35 = 0
idadef = 1000
ni = input ('Digite o n�mero de inscri��o: ')
while ni != 0:
    idade = input ('Digita a idade do candidato: ')
    sexo = raw_input ('Digite o sexo do candidato, "f" para mulher e "m" para homem: ')
    exp = raw_input ('Digite "sim" caso haja experiencia e "n�o" caso n�o haja: ')
    if sexo == "f":
        contf += 1
    else:
        contm += 1
    if sexo == 'm' and exp == 'sim':
        somai += idade
        conti +=1
    if sexo == 'm' and idade > 45:
        contm45 += 1
    if sexo == 'f' and exp == 'sim' and idade < 35:
        contf35 += 1
    if idadef > idade and exp == 'sim' and sexo == 'f':
        idadef = idade
    ni = input ('Digite o n�mero de inscri��o: ')    
percm45 = (contm45/float(contm))*100
print 'Candidatas mulheres: ', contf
print 'Candidatos homens: ', contm
print 'Idade m�dia dos homens com experi�ncia: ', somai/conti
print percm45, '% dos homens acima dos 45 anos tem experi�ncia.'
print contf35, 'mulheres abaixo dos 35 tem experi�ncia.'
print 'A mulher mais jovem com experi�ncia tem ', idadef, 'anos.'
