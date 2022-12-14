import math

def pascal_tri(numRows):
    #Print Pascal's triangle with numRows.
    for i in range(1,numRows):
        # loop to get elements of row i
        for j in range(i + 1):
            # nCr = n!/((n-r)!*r!)
            print(math.factorial(i) // (math.factorial(j) * math.factorial(i - j)), end=" ")

        # print each row in a new line
        print("\n")






n=int(input("donnez un nombre"))



def pascalSpot(row,col):
    if (col==1):
        return 1
    if (col==row):
        return 1
    lf=pascalSpot(row-1,col-1)
    rg=pascalSpot(row-1,col)
    return lf+rg
for r in range(n, 0, -1):
    for c in range(r,0,-1):
        print(pascalSpot(r,c),end=" ")
    print("")
pascal_tri(n)




