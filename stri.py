namaku = input('Nama = ')
print ('Belum diubah =' , namaku)
pengubah = namaku [:10] + input('Nama lain = ' +  namaku [:10] )
print ('Sudah diubah = ' ,pengubah)
a = namaku[:10] + " " + namaku[:10]
#penggunaan replace
kata = input("Masukkan namamu : ")
kata = kata.replace("B", "O")
kata = kata.replace("A", "L")
kata = kata.replace("K", "E")
kata = kata.replace("I", "D")
print("Namamu yang telah diganti:", kata)
kata = input("Masukkan namamu : ")
tabel = str.maketrans("BAKI", "OLED")
kata_ganti = kata.translate(tabel)
print("Namamu yang telah diganti:", kata_ganti)
