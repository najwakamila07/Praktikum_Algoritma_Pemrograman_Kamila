# ==========================================================
# PRAKTIKUM ALGORITMA & PEMROGRAMAN: BAGIAN 12
# Topik : Fungsi
# Nama  : Najwa Kamila
# NPM   : 2605060018
# Prodi : Teknologi Informasi
# ==========================================================

import math

# a. Fungsi menghitung luas persegi panjang
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

# b. Fungsi menghitung volume persegi panjang (balok)
def volume_persegi_panjang(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

# c. Fungsi menghitung luas lingkaran
def luas_lingkaran(jari_jari):
    return math.pi * (jari_jari ** 2)

# d. Fungsi menghitung volume bola
def volume_bola(jari_jari):
    return (4 / 3) * math.pi * (jari_jari ** 3)


print("=== PROGRAM HITUNG BANGUN DATAR & RUANG ===")

# a. Luas persegi panjang
print("\n1. Luas Persegi Panjang")
p_luas = float(input("Masukkan panjang : "))
l_luas = float(input("Masukkan lebar   : "))
print(f"Luas persegi panjang = {luas_persegi_panjang(p_luas, l_luas):.2f}")

# b. Volume persegi panjang
print("\n2. Volume Persegi Panjang")
p_vol = float(input("Masukkan panjang : "))
l_vol = float(input("Masukkan lebar   : "))
t_vol = float(input("Masukkan tinggi  : "))
print(f"Volume persegi panjang = {volume_persegi_panjang(p_vol, l_vol, t_vol):.2f}")

# c. Luas lingkaran
print("\n3. Luas Lingkaran")
r_lingkaran = float(input("Masukkan jari-jari : "))
print(f"Luas lingkaran = {luas_lingkaran(r_lingkaran):.2f}")

# d. Volume bola
print("\n4. Volume Bola")
r_bola = float(input("Masukkan jari-jari : "))
print(f"Volume bola = {volume_bola(r_bola):.2f}")