# -*- coding: utf-8 -*-
soma1 = 0
soma2 = 0
num = [1.0]*10
for i in range (0, 10):
    num[i] = float(input('Número: '))
    print 'Vetor:', num
    
for i in range (0, 10):
    if num[i]%2 == 0:
        soma2 += num[i]
    if i%2 != 0:
        soma1 += num[i]
res = soma2 - soma1
print res
