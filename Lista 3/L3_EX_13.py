# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 3: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 13

conts = 0.0
contn = 0.0
r = raw_input ('Você está satisfeito(a) com o novo produto? responda (S) ou (N): ')
while r.lower() != 'f':
    if r.lower() == 's':
        conts += 1
    else:
        contn +=1
    r = raw_input ('Você está satisfeito(a) com o novo produto? responda (S) ou (N): ')
s = (conts/(conts + contn))*100
n = (contn/(conts + contn))*100
print s, '% das pessoas disseram que sim e ', n, '% das pessoas disseram que não'
