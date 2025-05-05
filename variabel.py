name = input ("Namamu: ")
back = input ("Nama Belakang: ")
umur = int(input("Umurmu: ")) 
if umur <= 19:
    print ("Remaja")
elif umur >= 20:
    print("Dewasa")
else :
    print("Anak Anak") 
print (umur)
print(type(umur))

print(f"{name} {back} Ultra {umur}")
