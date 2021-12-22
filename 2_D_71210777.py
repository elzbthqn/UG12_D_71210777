KiKo = input("Hi Kiko, Silahkan Masukkan hari yang ingin Anda telusuri: ")

senin = ["Kelas ke-1 Algorima Graf","Kelas ke-3 Sistem Operasi","Kelas ke-4 PAK"]
for i in range(len(senin)):
    print("kelas ke-%d %s" % (i+1, senin[i]))