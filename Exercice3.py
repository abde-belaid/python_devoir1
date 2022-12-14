
# mot="abracabadra"
# cle="ista"
mot = input("donnez votre mot de passe à chiffre: ").upper()
cle = input("donnez votre cle: ").upper()
a = len(mot)
b = len(cle)
c = a // b
d = a - (b * c)
print(mot)
crypt=cle * c + cle[:d].upper()
print(crypt)
#creation de tableau
t=[]
for row in range(26):
    t.append([])

for row in range(26):
    for column in range(26):
        if (row+65)+column>90:
            t[row].append(chr((row+65+column-26)))
        else:
            t[row].append(chr((row+65+column)))
for row in t:
    for column in t:
        print(column)
li=[]

for x in mot:
    for j in crypt:
        li.append(t[mot.index(x)][crypt.index(j)])
print(li)