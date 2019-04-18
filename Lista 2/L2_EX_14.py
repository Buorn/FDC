# -*- coding: cp1252 -*-
#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 2: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 14
a = float (input ('Quantidade de votos do candidato Capitão Gancho: '))
b = float (input ('Quantidade de votos do candidato Peter Pan: '))
c = float (input ('Quantidade de votos do candidato Wendy: '))
a1 = (a/(a+b+c))*100
a2 = (b/(a+b+c))*100
a3 = (c/(a+b+c))*100
print ' Candidato Capitão Gancho tem', a1, '% dos votos'
print ' Candidato Peter Pan tem', a2, '% dos votos'
print ' Candidato Wendy tem', a3, '% dos votos'
if a1 < 50 and a2 < 50 and a3 <50:
    if (a1 < a2 and a2 <a3) or (a1 < a3 and a3 < a2):
        print 'Segundo turno entre Wendy com', a3, '% dos votos e Peter Pan com', a2, '% dos votos'
    elif (a2 < a1 and a1 <a3) or (a2 < a3 and a3 < a1):
        print 'Segundo turno entre Wendy com', a3, '% dos votos e Capitão Gancho com', a1, '% dos votos'
    elif (a3 < a1 and a1 <a2) or (a3 < a2 and a2 < a1):
        print 'Segundo turno entre Peter Pan com', a2, '% dos votos e Capitão Gancho com', a1, '% dos votos'
elif a1 > 50: 
    print   'Capitão Gancho foi eleito no primeiro turno com', a1, '% dos votos'
elif a2 > 50:
    print   'Peter Pan foi eleito no primeiro turno com', a2, '% dos votos'
else:
    print   'Wendy foi eleito no primeiro turno com', a3, '% dos votos'
