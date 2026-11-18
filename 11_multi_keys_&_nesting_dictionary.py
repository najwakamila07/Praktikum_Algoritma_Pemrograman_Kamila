untidar = {
    "Teknik" : {
        "Informasi" : {
            "nama" : "ucup",
            "npm" : 100
        },
        "Sipil" : {
            "nama" : "siti",
            "npm" : 70
        }
    }
}
print(untidar["Teknik"]["Sipil"]["nama"])
print(untidar["Teknik"]["Sipil"]["npm"])

import datetime

mahasiswa1 = {
    "nama": "Ucup Surucup",
    "sks_lulus": 130,
    "lahir": datetime.datetime(2001, 4, 10)
}

mahasiswa2 = {
    "nama": "Azar Magrib",
    "sks_lulus": 140,
    "lahir": datetime.datetime(2000, 1, 1)  # ganti sesuai aslinya
}

mahasiswa3 = {
    "nama": "Slamet Dunia Akhirat",
    "sks_lulus": 100,
    "lahir": datetime.datetime(2000, 1, 1)  # ganti sesuai aslinya
}

data_mahasiswa = {
    "MAH001": mahasiswa1,
    "MAH002": mahasiswa2,
    "MAH003": mahasiswa3,
}

print(data_mahasiswa["MAH003"]["nama"])

for key, mhs in data_mahasiswa.items():
    format_lahir = mhs['lahir'].strftime("tanggal %d bulan %m tahun %Y")
    print(f"{mhs['nama']} sudah lulus {mhs['sks_lulus']} SKS dan lahir pada {format_lahir}")

print(f"{'KEY':<6} | {'Nama':<20} | {'SKS':<3} | {'Lahir':<30}")
print("-" * 68)

for key, mhs in data_mahasiswa.items():
    format_lahir = mhs['lahir'].strftime("tanggal %d bulan %m tahun %Y")
    print(f"{key:<6} | {mhs['nama']:<20} | {mhs['sks_lulus']:<3} | {format_lahir:<30}")
mahasiswa = {}

mahasiswa["nama"] = input("Nama Mahasiswa: ")
mahasiswa["nim"] = input("NIM Mahasiswa: ")
mahasiswa["jurusan"] = input("Jurusan: ")

print(mahasiswa)
# Program 11.1
import datetime

mahasiswa1 = {
    'nama': 'Ucup Surucup',
    'nim': '19022001',
    'sks_lulus': 130,
    'beasiswa': False,
    'lahir': datetime.datetime(2001, 4, 10)  # tahun, bulan, tanggal
}
mahasiswa2 = {
    'nama': 'Azan Magrib',
    'nim': '19022002',
    'sks_lulus': 140,
    'beasiswa': True,
    'lahir': datetime.datetime(2002, 10, 10)
}
mahasiswa3 = {
    'nama': 'Slamet Dunia Akhirat',
    'nim': '19022003',
    'sks_lulus': 100,
    'beasiswa': True,
    'lahir': datetime.datetime(1977, 5, 10)
}

# nesting: dictionary di dalam dictionary
data_mahasiswa = {
    'MAH001': mahasiswa1,
    'MAH002': mahasiswa2,
    'MAH003': mahasiswa3,
}

print(f"{'KEY':<6} {'Nama':<20} {'SKS':<4} {'Beasiswa':<9} {'Lahir':<10}")
print("-" * 55)
for KEY in data_mahasiswa:
    NAMA = data_mahasiswa[KEY]['nama']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
    print(f"{KEY:<6} {NAMA:<20} {SKS:<4} {BEASISWA!s:<9} {LAHIR:<10}")

# Program 11.2
import datetime

mahasiswa_template = {
    'nama': 'nama',
    'nim': '00000000',
    'sks_lulus': 0,
    'lahir': datetime.datetime(1111, 1, 11)
}
data_mahasiswa = {}

print(f"{'SELAMAT DATANG':^20}")
print(f"{'DATA MAHASISWA':^20}")
print("-" * 20)

mahasiswa = dict.fromkeys(mahasiswa_template.keys())
print(mahasiswa)

mahasiswa['nama'] = input("Nama Mahasiswa: ")
mahasiswa['nim'] = input("NIM Mahasiswa: ")
mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))
mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

print(mahasiswa)

# Program 11.3
import datetime
import os
import string
import random

mahasiswa_template = {
    'nama': 'nama',
    'nim': '00000000',
    'sks_lulus': 0,
    'lahir': datetime.datetime(1111, 1, 11)
}
data_mahasiswa = {}

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-" * 20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input("Nama Mahasiswa: ")
    mahasiswa['nim'] = input("NIM Mahasiswa: ")
    mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
    TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
    BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
    TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

    # key acak 6 huruf besar
    KEY = ''.join(random.choice(string.ascii_uppercase) for i in range(6))
    data_mahasiswa.update({KEY: mahasiswa})

    print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<8} {'SKS Lulus':<10} {'Tanggal Lahir':<10}")
    print('-' * 60)
    for KEY in data_mahasiswa:
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
        print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10} {LAHIR:^10}")

    print("\n")
    is_done = input("Mau tambah lagi bro (y/n)? ")
    if is_done == "n":
        break

print("\nAkhir dari program, terima kasih")