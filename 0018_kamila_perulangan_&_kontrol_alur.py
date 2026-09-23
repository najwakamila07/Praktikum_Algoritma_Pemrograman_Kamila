# ==========================================================
# PRAKTIKUM ALGORITMA & PEMROGRAMAN: BAGIAN 5
# Topik : Latihan Perulangan (Ganjil-Genap & Bilangan Prima)
# Nama  : Najwa Kamila
# NPM   : 2605060018
# Prodi : Teknologi Informasi
# ==========================================================

print("=" * 45)
print("  LATIHAN 1: BILANGAN GANJIL & GENAP (1 - 50)  ")
print("=" * 45)

# Latihan 1: Menggunakan for dan range (seperti Program 5.1)
for i in range(1, 51):
    if i % 2 == 0:
        print(f"Angka {i} -> Genap")
    else:
        print(f"Angka {i} -> Ganjil")

print("\n" + "=" * 45)
print("     LATIHAN 2: BILANGAN PRIMA (1 - 100)     ")
print("=" * 45)

# Latihan 2: Menggunakan for, range, if, dan break (seperti Program 5.1 & 5.4)
print("Bilangan prima antara 1 sampai 100:")

for angka in range(1, 101):
    if angka > 1:
        is_prima = True
        for pembagi in range(2, angka):
            if angka % pembagi == 0:
                is_prima = False
                break  # Sesuai materi break di modul
        
        if is_prima == True:
            print(angka, end=" ")

print("\n" + "=" * 45)