b =''
a = raw_input ('Digite uma sequencia de DNA: ').upper()
for i in range (0,len(a)):
    if a[i].upper() == 'A':
        b += a[i].replace('A','T')
    elif a[i].upper() == 'T':
        b += a[i].replace('T','A')
    elif a[i].upper() == 'G':
        b += a[i].replace('G','C')
    elif a[i].upper() == 'C':
        b += a[i].replace('C','G')
print a ,':', b
