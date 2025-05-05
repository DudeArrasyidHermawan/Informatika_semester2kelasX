#pertambahan
print ("Pertambahan")
semangka1 = int(input("Berapa buah: "))
mangga2 = int(input("Berapa buah: "))
harga_semangka = 13000
harga_mangga = 12000
total = (semangka1 * harga_semangka) + (mangga2 * harga_mangga)
print("Total harga: Rp", total)
print ("")

#pengurangan
print ("Pengurangan")
bukuper = int(input("Berapa buku? "))
diskon = 13000
hargabuku = 18000 
keseluruh = (bukuper * hargabuku) - (diskon)
print (keseluruh)
print ("")

#perkalian
print ("Perkalian")
apel1 = int(input("Berapa banyak: "))
pisang2 = int(input("Berapa banyak:"))
harga_apel = 120
harga_pisang = 100
total_keseluruhan = (apel1 * harga_apel) * (pisang2 * harga_pisang)
print (total_keseluruhan)
print ("")

#pembagian 
print ("Pembagian")
donat = int(input("Masukkan: "))
puding = int(input("Masukkan: "))
sal_donat = 10
sal_pudin = 5
jumlah = (donat * sal_donat) / (puding * sal_pudin)
print (jumlah)
print("")

#Modulus
print("Modulus")
angka = int(input("Number? "))
angka2 = int(input("Number? "))
hasil_asli = angka % angka2
print ("Hasil dari bagi angka 1: ", angka, "Hasil dari bagi 2; ",angka2, "Yaitu : ", hasil_asli)
print ("")

#Pangkat
print("Pangkat")
bilangan_pengguna = int(input("Bilangan 1 :"))
bilangan2 = int(input("Bilangan 2 :"))
hasil = bilangan_pengguna ** bilangan2
print (hasil)
print("")

#Pembagian Bulat
print("Pembagian bulat")
print (100//3)
#Contoh kedua Pembagian Bulat
pembagian = int(input("Bilangan 1 : "))
pembagian2 = int(input("Bilangan 2 : "))
hasilnya = pembagian // pembagian2
print (hasilnya)