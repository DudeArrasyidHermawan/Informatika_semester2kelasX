x = 100
y = 100

print ("Sistem Operasi Perhitungan")
print ("Pertambahan(+)")
print ("Pengurangan(-)")
print ("Perkalian(*)")
print ("Pembagian(/)")

print ("=========================")
print ("Masukkan Angka Pertama = ", x)  
print ("Masukkan Angka Kedua = ", y)    
print ("=========================") 
kata = input("Pilih operasi diatas[|+|,|-|,|*|,|/|] ")

if kata == '+':
  print ("Hasil = ", x+y)
elif kata == '-':
    print ("Hasil = ", x-y)
elif kata == '*':
    print ("Hasil = ", x*y)
elif kata == '/':
    print ("Hasil = ", x/y)
else :
 print("Kode Operasi Perhitungan Salah")