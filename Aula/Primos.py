#NUMEROS PRIMOS
for n in range (1, 100):
    cont = 0
    for i in range (1,n+1):
        a = n%i
        if a == 0:
            cont += 1
    if cont == 2:
        print n
