# ==========================================================
# PRAKTIKUM ALGORITMA & PEMROGRAMAN: BAGIAN 4
# Topik : Logical, Komparasi Logical, dan ELIF
# Nama  : Najwa Kamila
# NPM   : 2605060018
# Prodi : Teknologi Informasi
# ==========================================================

print("=" * 40)
print("      PROGRAM PENGELOMPOKAN USIA        ")
print("=" * 40)

usia = int(input("Masukkan usia: "))
print("-" * 40)

if usia < 0:
    print("Kategori: Usia tidak valid!")
elif 0 <= usia <= 12:
    print("Kategori: Anak-anak")
elif 13 <= usia <= 17:
    print("Kategori: Remaja")
elif 18 <= usia <= 59:
    print("Kategori: Dewasa")
else:
    print("Kategori: Lansia")

print("=" * 40)