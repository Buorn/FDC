# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 5: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 10
def lerstring(): #LER STRING
    s=raw_input('Digite frase: ')
    return s


def vogal(f): #CONTA A QUANTIDADE DE VOGAIS DA STRING
    v=0
    for i in range(0,len(f)):
        if f[i].lower()=='a' or f[i].lower()=='e' or f[i].lower()=='i' or f[i].lower()=='o' or f[i].lower()=='u':
            v+=1
    return v


def branco(f): #CONTA A QUANTIDADE DE ESPA�OS DA STRING
    b=0
    for i in range(0,len(f)):
        if f[i]==' ':
            b+=1
    return b


def outros(f): #CONTA A QUANTIDADE DE OUTROS CARACTERES DA STRING
    o=len(f)-(branco(frase)+vogal(frase))
    print 'Outros:', o


#PROGRAMA PRINCIPAL
frase=lerstring()
print 'Vogais:',vogal(frase)
print 'Espa�os em branco:',branco(frase)
outros(frase)

    
