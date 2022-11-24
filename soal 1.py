print ("~~~~~~~~~~~~/('V')\~~~~~~~~~~~~~~~")
print ("PROGRAM PENGHITUNG VOLUME BANGUN RUANG")
print ("~~~~~~~~~~~~/('V')\~~~~~~~~~~~~~~~")
print ("Pilihlah salah satu bangun ruang yang ingin di hitung volumenya :")
print ("1.Limas")
print ("2.Bola")
print ("3.Prisma")
print ("4.Kerucut")
e = int (input ("Masukkan pilihan anda :"))
if e == 1 :
    ab = int (input ("Masukkan panjang sisi alas limas :"))
    ac = int (input ("Masukkan tinggi limas :"))
    limas = 1/3 * ab * ac
    print ("Volume Limas tersebut adalah :",limas)
elif e == 2 :
    ba = int (input ("masukan jari jari bola :"))
    bola = (4/3) * 3.14 * ba
    print ("Volume Bola tersebut adalah :",bola) 
elif e == 3 :
    ca = int (input ("Masukkan sisi prisma :"))
    cb = int (input ("Masukkan apotema prisma"))
    cc = int (input ("Masukkan tinggi prisma :"))
    prisma = 1/2 (5 * ca * cb) * cc
    print ("Volume Prisma adalah :",prisma)
else :
    da = int (input ("Masukkan jari jari kerucut : "))
    db = int (input ("Masukkan tinggi kerucut :"))
    kerucut = 1/3 * 3.14 * da * da * db
    print ("Volume kerucut tersebut adalah :",kerucut)
