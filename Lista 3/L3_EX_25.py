# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 3: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 25
m_cand_vaga = 0
m_cod = 0
soma = 0
cod = input ('Digite o código do curso: ')
while cod != 0:
    nv = float (input ('Digite o número de vagas do curso: '))
    ncm = float (input ('Digite o número de canditados do sexo masculino: '))
    ncf = float (input ('Digite o número de canditados do sexo feminino: '))
    cand = ncm + ncf
    soma += cand
    cand_vaga = cand/nv
    perc_fem = (ncf/(ncf +ncm))*100
    if m_cand_vaga < cand_vaga:
        m_cand_vaga = cand_vaga
        m_cod = cod
    print cand_vaga, 'candidatos por vaga no curso ', cod
    print perc_fem, '% dos candidatos do curso', cod, 'são mulheres.'
    cod = input ('Digite o código do curso: ')
print 'O curso', m_cod, 'teve o maior número de candidatos por vagas: ', m_cand_vaga
print 'O número total de candidatos é: ', soma        
        
