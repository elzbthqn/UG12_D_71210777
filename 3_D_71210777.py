l = int(input("Masukkan Angka : "))
print()

for i in range (l) :
    for j in range (l,i,-1) :
        print(" ",end = "")
    for j in range (2*i+1) :
        print("*", end = "")
    print()

for i in range (l-1,-1,-1) :
    for j in range (l,i,-1) :
        print( " ",end = "")
    for j in range (2*i+1) :
        print("*",end = "")
    print()