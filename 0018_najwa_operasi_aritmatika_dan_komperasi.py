# ===========================================
# PRAKTIKUM OPERASI ARITMATIKA DAN KOMPERASI 
# Nama : Najwa Kamila
# NPM : 2605060018
# Prodi : Teknologi Informasi
# ===========================================

# DIKETAHUI
# Simpan angka yang ada di soal ke variabel
panjang = 12
lebar = 5
tinggi = 8
# Tampilkan data yang udah diketahui
print("DIKETAHUI")
print("Panjang :", panjang)
print("Lebar   :", lebar)
print("Tinggi  :", tinggi)

# DITANYA
print("DITANYA = Luas, Volume, dan Keliling?")

# JAWAB
# Rumus luas permukaan balok = 2 x ( (p*l) + (p*t) + (l*t) )
luas = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))

# Rumus volume balok = p x l x t
volume = panjang * lebar * tinggi

# Rumus keliling balok = 4 x (p + l + t)
keliling = 4 * (panjang + lebar + tinggi)
# Tampilkan data jawaban
print("JAWABAN POIN A")
print("Luas Permukaan :", luas)
print("Volume         :", volume)
print("Keliling Rusuk :", keliling)


# DITANYA
# Apakah luas bangunan lebih dari 50?
# Cek pake komparasi, apakah luasnya lebih gede dari 50?
cek_luas = luas > 50
#Tampilkan data jawaban
print("JAWABAN POIN B")
print("Apakah luas lebih gede dari 50? :", cek_luas)


# DITANYA 
# Apakah volumenya bernilai 480?
# Cek pake komparasi, apakah volumenya pas 480?
cek_volume = volume == 480
# Tampilkan data jawaban
print("JAWABAN POIN C")
print("Apakah volumenya bernilai 480?  :", cek_volume)