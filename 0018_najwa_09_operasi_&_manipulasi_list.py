# ==========================================================
# PRAKTIKUM ALGORITMA & PEMROGRAMAN: BAGIAN 9
# Topik : Operasi dan manipulasi List
# Nama  : Najwa Kamila
# NPM   : 2605060018
# Prodi : Teknologi Informasi
# ==========================================================

print("===== Soal 1 =====")
kendaraan = ['motor', 'mobil', 'sepeda', 'bus']

kendaraan.append('truk')           # a. Tambahkan 'truk' di akhir list 
print(kendaraan)

kendaraan.insert(1, 'becak')       # b. Sisipkan becak' pada index ke-1 
print(kendaraan)

kendaraan.pop()                    # c. Hapus data yang berada paling belakang  
print(kendaraan)

kendaraan[kendaraan.index('sepeda')] = 'skuter'   # d. Ubah elemen 'sepeda' menjadi 'skuter'
print(kendaraan)

print(len(kendaraan))              # e. i Jumlah total data di dalam list

print("===== Soal 2 =====")
angka = [75, 80, 90, 75, 85, 100, 65]

print(angka.index(100))            # a. indeks ke berapa skor 100 berada?. -> 5 
print(angka.count(75))             # b. ada berapa banyak siswa yang mendapatkan skor 75?. -> 2

angka.sort()                       # c. Urutkan list skor_ujian tersebut dari nilai terkecil hingga terbesar. 
print(angka)                       

angka.reverse()                    # d. Balikkan urutan list yang sudah diurutkan tersebut sehingga menjadi dari terbesar ke terkecil. 
print(angka)                       

print("===== Soal 3 =====")
menu_utama = ["Nasi Goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]

menu_utama.extend(menu_tambahan)
print(menu_utama)   

print("===== Soal 4 =====")
data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]

print(data_barang[1][1])           # a -> 2000

for b in data_barang:              # b
    print(f"Nama: {b[0]}, Harga: {b[1]}")