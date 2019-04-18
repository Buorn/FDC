# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 5: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 9
def lerString(): #LER STRING
    s=raw_input('Digite a frase: ')
    return s

def palavra(f): #SEPARA AS PALAVRAS DE UMA FRASE
    palavra=f.split()
    for i in range(0,len(palavra)):
        print palavra[i]

#PROGRAMA PRINCIPAL
frase=lerString()
palavra(frase)
