mat = []
for i in range(0,4):
    mat.append(0)
    mat[i] = []
    for j in range(0,4):
        mat[i].append(int(input("elem:")))

for line in mat:
    print "%4d %4d %4d %4d" % tuple(line)
