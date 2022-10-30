#Masukkan tinggi diamod
tinggi= int(input("Masukkan tingginya :"))

#lakukan perulangan agar menjadi diamond
for i in range(1, tinggi, 2):
    print(" "*(tinggi//2-i//2), "*"*i)
for i in range(tinggi, 0, -2):
    print(" "*(tinggi//2-i//2), "*"*i)