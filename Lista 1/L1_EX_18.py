#UNIVERSIDADE DO ESTADO DO RIO DE JANEIRO - UERJ
#BRUNO BANDEIRA BRANDÃO
#LISTA 1: FUNDAMENTOS DA COMPURAÇÃO 2018/2
#EXERCÍCIO 18
dtotal = input ('Digite o número de dias:')
a = dtotal//365
m = (dtotal%365)//30
d = (dtotal%365)%30
print dtotal, 'dia(s) =', a, 'ano(s)', m,'mes(es)', d, 'dia(s)' 
