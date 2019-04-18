vetor = []
for i in range (0,5):
    vetor.append(input('nota: '))
print 'VETOR: ', vetor


for i in range (0,4):
    for j in range (i+1,5):
        if vetor[i]>vetor[j]:
            aux=vetor[i]
            vetor[i]=vetor[j]
            vetor[j]=aux
print 'Vetor ordenado:', vetor
