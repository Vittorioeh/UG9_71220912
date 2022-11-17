kecepatan = int(input("Masukkan kecepatan tempuh :"))
waktu = int(input("Masukkan waktu yang diperlukan :"))

#rumus
bensin = kecepatan*waktu / 10
biaya = bensin * 15000

print ("Teman anda mengisi bensin sebanyak" , bensin , "liter")
print ("Biaya yang dikeluarkan untuk mengisi bensin adalah Rp." , biaya)
