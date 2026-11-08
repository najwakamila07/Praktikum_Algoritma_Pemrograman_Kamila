# ==========================================================
# PRAKTIKUM ALGORITMA & PEMROGRAMAN: BAGIAN 10
# Topik : Tuples, Set, dan Dictionary
# Nama  : Najwa Kamila
# NPM   : 2605060018
# Prodi : Teknologi Informasi
# ==========================================================

print("===== Soal 1 =====")

print("a. Membuat tuple mahasiswa")
mahasiswa = ("Najwa Kamila", "2605060018", "Teknologi Informasi")   
print(mahasiswa)

print("b. Menampilkan NIM dan Prodi")
print(mahasiswa[1])                
print(mahasiswa[2])                

print("c. Mengubah isi tuple")
# mahasiswa[2] = "Teknologi Informasi"   
print("Error terjadi karena Tuple itu immutable (tidak dapat diubah), jadi isinya tidak bisa diubah, ditambah, atau dihapus.")

print("d. Membuat set nilai_angka")
nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}   
print(nilai_angka)
print("Angka 10 dan 4 yang ditulis dua kali cuma disimpan satu kali, karena set otomatis menghapus nilai yang kembar.")

print("===== Soal 2 =====")

print("a. Membuat dictionary data_mahasiswa")
data_mahasiswa = {                 
    "nim": "240101",
    "nama": "Budi Santoso",
    "prodi": "Teknologi Informasi"
}
print(data_mahasiswa)

print("b. Mengubah prodi dan menambah angkatan")
data_mahasiswa["prodi"] = "Sastra Mesin"   
data_mahasiswa["angkatan"] = 2026          
print(data_mahasiswa)

print("c. Menghapus nim")
del data_mahasiswa["nim"]          
print(data_mahasiswa)

print("===== Soal 3 =====")

print("a. Membuat dictionary keranjang")
keranjang = {"apel": 5000, "pisang": 3000, "jeruk": 7000, "anggur": 15000}   
print(keranjang)

print("b. Menampilkan setiap barang dan harganya")
total = 0
for key,value in keranjang.items():        
    print(f"Harga {key}: Rp {value}")
    total += value                         

print("c. Total belanja")
print(f"Total belanja: Rp {total}")        