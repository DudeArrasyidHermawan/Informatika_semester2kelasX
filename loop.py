number = int(input("Masukkan nomor: "))
for a in range(number) :
    print (a)

kesukaan = input(" Makanan: ")
for b in kesukaan :
    print (b)
makanan = input(" Makanan Ringan: ")
for c in makanan :
    print (c)
data = int(input(" Nomor Data yang dibutuhkan: "))
while (data <= 1002):
    print (" Nomor Data nya Adalah:", data)
    data +=1

hari_ini = int(input("Masuk kan hari apa: "))
if hari_ini == 0:
    hari = 'Senin'
elif hari_ini == 1:
    hari = 'Selasa'    

elif hari_ini == 2:
    hari = 'Rabu'
    
elif hari_ini == 3:
    hari = 'Kamis'

elif hari_ini == 4:
    hari = 'Jumat'
    
elif hari_ini == 5:
    hari = 'Sabtu'
    
elif hari_ini == 6:
    hari = 'Minggu'
else :
    hari = "Bukan 7 Hari di Bumi"
print(hari)    

variabel = int(input("Masukkan Nomormu Washoi!!!"))
while variabel <= 1000:
    print("The number is :", variabel)
    variabel += 10

