n=int(input("donner la longueur du tableau : "))
t1=[]
for x in range(n):
    g=str(input(f"doner le chiffre N{x+1}:"))
    t1.append(g.upper())
print(t1)
for j in range(n):
    m = ord(t1[j])
    k = str
    j = 0
    t2 = []
    for i in range(1,len(t1)):
        if ord(t1[i])<m:
            k=t1[i]
            j=i
            m=ord(k)
    t1[j]="a"
    t2.append(k)
t2=sorted(t1)
print(t2)