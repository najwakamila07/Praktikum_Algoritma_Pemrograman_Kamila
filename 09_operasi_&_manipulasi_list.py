print("LATIHAN OPERASI & MANIPULASI LIST")
print("=" *40)

print("program 9.1")
print("bagian 1 : list biasa")
data_int = [1, 2, 3, 4, 5]
data_string = ["ucup", "asep", "bambang"]
data_boolean = [True, False, True, True]
data_campuran = ["bakwan", 1, True, 4 ]
print(data_campuran)
print(data_int)

print("bagian 2 : list dari range")
data_range = range(0, 10, 2)
print(data_range)
data_list = list(data_range)
print(data_list)

print("bagian 3 : list comprehension")
# dikuadratkan setiap angkanya
print([i**2 for i in range(0, 10)])
# semua angka kecuali 3
print([i for i in range(0, 10) if i!= 3])
# semua angka genap
print([i for i in range (0, 10) if i % 2 == 0])
# semua angka ganjil
print([i for i in range (0, 15) if i % 2 != 0])

# latihan yang diluar modul
data_buah = ["apel", "mangga", "jeruk"]
print(data_buah)
data_angka = [1, 5, 8, 9]
print(data_angka)
data_bool = [True, False, False, True]
print(data_bool)
data_cmpr = [1, "alpukat", True, "hijau"]
print(data_cmpr)
data_rge = range(0, 10, 3)
print(data_rge)
data_lst = list(data_rge)
print(data_lst)
print([i**2 for i in range(1,6)])
print([i for i in range(0, 11) if i % 2 == 0])

print("Program 9.2: Tambah, ubah, hapus isi list")
data = ["Ucup", "Adit", "Dudung"]
#index    0       1        2    
#mengambil data
print(data[0])
print(data[-1]) #terakhir
print(len(data))
#menambah data
data.insert(1, "Asep")    
print(data) 
data.append("Ririn")      
print(data)    
data.extend(["Luffy", "Zoro", "Nami"])   
print(data)    
data[2] = "jarwo"    
print(data)   
#menghapus data
data.remove("Ucup")   
data.pop()            
print(data)    

#latihan diluar modul
teman = ["budi", "sari", "doni"]
print(teman[0])
print(teman[-1])
print(len(teman))
teman.insert(1, "andi")
print(teman)
teman.append("Rina")
teman.extend(["tono", "yuli"])
teman[2] = "sinta"
print(teman)
teman.remove("budi")
teman.pop()
print(teman)

# Program 9.3: Hitung, cari, urutkan, balik
# Hitung berapa kali muncul (count)
data_angka = [1, 5, 1, 4, 3, 2, 4, 3, 2, 3, 7, 8, 9, 0]
print(data_angka.count(4))   
print(data_angka.count(3))   
# Cari posisi (index)
data = ["Rendi", "Iqbal", "Gana", "Khairil"]
print(data.index("Iqbal"))   
print(data.index("Gana"))    
# urutan (sort)
data_angka.sort()
print(data_angka)   
data.sort()
print(data)        
data_angka.reverse()
print(data_angka)   
 
latihan diluar modul
skor = [70, 85, 90, 70, 60, 100, 70, 85]
nama = ["Dewi", "Agus", "Citra", "Bayu"]
print(skor.count (70))
print(skor.count (85))
print(nama.index("Citra"))
skor.sort()
print(skor)
nama.sort()
print(nama)
skor.reverse()
print(skor)

# Nested list: list di dalam list
data_0 = [1, 2]
data_1 = [3, 4]
list_2D = [data_0, data_1]
print(list_2D)   
print(list_2D[0])      
print(list_2D[1][0])  
print(list_2D[1][1])   

peserta_0 = ["Rendi", 25, "Laki-laki"]
peserta_1 = ["Joni", 10, "Laki-laki"]
peserta_2 = ["Eka", 50, "Wanita"]

list_peserta = [peserta_0, peserta_1, peserta_2]

for peserta in list_peserta:
    print(f"nama\t : {peserta[0]}")
    print(f"umur\t : {peserta[1]}")
    print(f"Gender\t : {peserta[2]}\n")

siswa = [["Rina", 80], ["Doni", 75], ["Sari", 90]]

for s in siswa:
    print(f"Nama: {s[0]}, Nilai: {s[1]}")
 



