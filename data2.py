nama = input ('nama siswa? ')
#Boolean
keterangan = True
lulus = False

print (type(keterangan))
print (lulus)

#tipe data String

print (f"Hai {nama} Salam kenal",
       f"Kita bertemu lagi {nama} di tempat ini")
print (f'Ayo belajar kembali bersamaku {nama}')

#tipe data Integer
nomor1 = input ("kelas? ")
nomor2 = input ("Nomor bangku? ")
print (f"Kelasmu berada di nomor {nomor1} ",
       f"Nomor bangku-mu berada di {nomor2}")

#tipe data Float

nilai = 3.14 
angka = float(input("Angka yang kau masukkan: "))
rumus = angka * nilai
print("Hasil dari: ", rumus)

#tipe data Hexadecimal

print ("Bentuk Hexadecimal dari angka 16 adalah: " + hex(16))

print (f"{nama} " + " Bagasin ")

#tipe data Complex
print (3j)
print (1j)

#tipe data List
buah = ("Pisang","Apel","Mangga","Semangka")
angka = ("10","11","12","13")

print (buah[1], buah[2])
print (angka[0],angka[3])

#tipe data Tuple
print ((5,2,3,1,9))
print (("satu","tiga","lima"))

#tipe data Dictionary
print({"nama mu adalah": nama, "umur": 31})

#tipe data Dictionary dimasukan ke dalam variabel biodata
biodata = {"nama mu adalah": nama, "umur": 31}
print(biodata)
print(type(biodata))