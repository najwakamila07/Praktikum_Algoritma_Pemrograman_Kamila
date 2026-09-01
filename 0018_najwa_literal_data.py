# ===========================================
# PRAKTIKUM LITERAL DATA 
# Nama : Najwa Kamila
# NPM : 2605060018
# Prodi : Teknologi Informasi
# ===========================================

#Tugas 1 - Deklarasi variabel
nama = "Najwa Kamila"
umur = 18
berat = 45.0
print("Nama :", nama)
print("Umur :", umur, "tahun")
print("Berat Badan :", berat, "kg")

#Tugas 2 - Mengubah Tipe Data
# 1. Konversi string menjadi integer
data_str = "123"
data_int = int(data_str)
print("data = ", data_int, "type =", type(data_int))

# 2. Konversi float menjadi integer
data_float = 45.67
data_int = int(data_float)
print("data = ", data_int, "type =", type(data_int))

# 3. Konversi integer menjadi float
data_int = 89
data_float = float(data_int)
print("data = ", data_float, "type =", type(data_float))

# 4. Konversi integer menjadi string
data_int = 89
data_str = str(data_int)
print("data = ", data_str, "type =", type(data_str))

# Tugas 3 - Input Data
# a. Input usia dalam bentuk integer
usia = int(input("\nMasukkan usia: "))
print("data =", usia, "tahun", ", type =", type(usia))

# b. Input tinggi badan dalam bentuk float
tinggi_badan = float(input("\nMasukkan tinggi badan: "))
print("data =", tinggi_badan, "cm", ", type =", type(tinggi_badan))

# c. Input nama dalam bentuk string
nama = str(input("\nMasukkan nama: "))
print("data =", nama, ", type =", type(nama))
