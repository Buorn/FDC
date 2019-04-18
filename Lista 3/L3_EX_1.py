# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 3: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 1
cm = 0
cf = 0
ms = 0
ssm = 0
ssf = 0
idade = input ('Digite a idade do funcionario: ')
while idade > 0:
    sexo = raw_input ('Digite o sexo do funcionario (M) ou (F): ')
    salario = float( input ('Digite o salario do funcionario: '))
    if sexo == 'M' or sexo == 'm':
        ssm = ssm + salario
        cm += 1
    else:
        ssf = ssf + salario
        cf += 1
    if idade < 30 and salario > ms:
        ms = salario
    idade = input ('Digite a idade do funcionario: ')
mm = ssm/cm
mf = ssf/cf    
print 'Media salarial dos homens:', mm
print 'Media salarial das mulheres:', mf
print 'Maior salario para quem esta abaixo dos 30 anos:', ms
