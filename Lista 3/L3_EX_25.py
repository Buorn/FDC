# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRAND�O
#LISTA 3: FUNDAMENTOS DA COMPURA��O 2018/2
#EXERC�CIO 25
m_cand_vaga = 0
m_cod = 0
soma = 0
cod = input ('Digite o c�digo do curso: ')
while cod != 0:
    nv = float (input ('Digite o n�mero de vagas do curso: '))
    ncm = float (input ('Digite o n�mero de canditados do sexo masculino: '))
    ncf = float (input ('Digite o n�mero de canditados do sexo feminino: '))
    cand = ncm + ncf
    soma += cand
    cand_vaga = cand/nv
    perc_fem = (ncf/(ncf +ncm))*100
    if m_cand_vaga < cand_vaga:
        m_cand_vaga = cand_vaga
        m_cod = cod
    print cand_vaga, 'candidatos por vaga no curso ', cod
    print perc_fem, '% dos candidatos do curso', cod, 's�o mulheres.'
    cod = input ('Digite o c�digo do curso: ')
print 'O curso', m_cod, 'teve o maior n�mero de candidatos por vagas: ', m_cand_vaga
print 'O n�mero total de candidatos �: ', soma        
        
