# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 5: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 14
def lerstring(): #LER STRING
    s=raw_input('Ditite uma palavra: ')
    return s


def verifica(s): #VERIFICA SE A STRING � UM PALINDROMO
    cont=0
    for i in range(0,len(s)/2):
        if s[i]==s[len(s)-1-i]:
            cont+=1
    if cont==len(s)/2:
        print '� Palindromo!'
    else:
        print 'N�o � Palindromo!'


#PROGRAMA PRINCIPAL     
palavra=lerstring()
verifica(palavra)
