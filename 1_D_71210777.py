ang1 = int(input("Masukkan awal deret : "))
ang2 = int(input("Masukkan akhir deret : "))

x = []

if (ang1 + 1) % 2 == 0:
    for i in range (ang1+1,ang2,2):
        if i % 3 == 0 or i % 7 == 0: continue
        print ( i , end = " " )
else:
    for i in range (ang1 , ang2 , 2):
        if i % 3 == 0 or i % 7 == 0 : continue
        print (i , end = " ")