# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 5: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 1
def cVet(v): #CRIA VETOR
    for i in range(0,5):
        v.append(float(input('Digite a nota do Aluno: ')))
    return v


def media(v): #RETORNA A M�DIA DOS VALORES DO VETOR
    soma=0
    for i in range(0,len(v)):
        soma+=v[i]
    med=soma/len(v)
    return med


def maior(v): #RETORNA A QUANTIDADE DE VALORES MAIORES QUE A M�DIA DO VETOR
    maior=0
    for i in range(0,len(v)):
        if v[i]>media(v):
            maior+=1
    return maior


def igual(v): #RETORNA A QUANTIDADE DE VALORES IGUAIS QUE A M�DIA DO VETOR
    igual=0
    for i in range(0,len(v)):
        if v[i]==media(v):
            igual+=1
    return igual


def menor(v): #RETORNA A QUANTIDADE DE VALORES MENORES QUE A M�DIA DO VETOR
    menor=0
    for i in range(0,len(v)):
        if v[i]<media(v):
            menor+=1
    return menor


#PROGRAMA PRINCIPAL
vet = []
vet=cVet(vet)
print 'M�dia da Turma: ',media(vet)
print maior(vet), 'nota(s) maior(es) que a m�dia da turma.' 
print igual(vet), 'nota(s) igual(is) que a m�dia da turma.'
print menor(vet), 'nota(s) menores(es) que a m�dia da turma.'
