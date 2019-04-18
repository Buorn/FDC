# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 5: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 9
def lerString(): #LER STRING
    s=raw_input('Digite a frase: ')
    return s


def palavra(v,f): #SEPARA AS PALAVRAS DE UMA FRASE
    soma=' '
    for i in range(0,len(f)):
        v[i]=f[i]
    for i in range(0,len(v1)):
        if v1[i].isalpha():
            soma+=v1[i]
        else:
            print soma
            soma=' '
    print soma
    

#PROGRAMA PRINCIPAL
frase=lerString()
v1=['']*len(frase)
palavra(v1,frase)
