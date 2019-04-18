# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 3: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 26
contf = 0
contm = 0
somai = 0
conti = 0
contm45 = 0
contf35 = 0
idadef = 1000
ni = input ('Digite o número de inscrição: ')
while ni != 0:
    idade = input ('Digita a idade do candidato: ')
    sexo = raw_input ('Digite o sexo do candidato, "f" para mulher e "m" para homem: ')
    exp = raw_input ('Digite "sim" caso haja experiencia e "não" caso não haja: ')
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
    ni = input ('Digite o número de inscrição: ')    
percm45 = (contm45/float(contm))*100
print 'Candidatas mulheres: ', contf
print 'Candidatos homens: ', contm
print 'Idade média dos homens com experiência: ', somai/conti
print percm45, '% dos homens acima dos 45 anos tem experiência.'
print contf35, 'mulheres abaixo dos 35 tem experiência.'
print 'A mulher mais jovem com experiência tem ', idadef, 'anos.'
