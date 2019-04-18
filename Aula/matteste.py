mat1 = []
for i in range(0,4):
    mat1.append(0)
    mat1[i] = []
    for j in range(0,5):
        mat1[i].append(int(input("elem:")))
print mat1

vet=[0]*20
for i in range(0,4):
    for j in range(0,5):
        vet[i*5 + j] = mat1[i][j]

print "vet:", vet
