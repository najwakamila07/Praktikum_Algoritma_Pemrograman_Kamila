# ==========================================================
# PRAKTIKUM ALGORITMA & PEMROGRAMAN: BAGIAN 11
# Topik : Multi-Keys & Nesting Dictionary
# Nama  : Najwa Kamila
# NPM   : 2605060018
# Prodi : Teknologi Informasi
# ==========================================================

import datetime
import os
import string
import random

# Template dictionary buku perpustakaan
buku_template = {
    'judul': 'judul',
    'penulis': 'penulis',
    'tahun_terbit': 0,
    'terakhir_pinjam': datetime.datetime(1111, 1, 11),
    'status': 'TERSEDIA'
}

data_perpustakaan = {}

while True:
    # Membersihkan layar terminal (otomatis menyesuaikan Windows / Mac / Linux)
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{'SELAMAT DATANG':^40}")
    print(f"{'SISTEM MANAJEMEN PERPUSTAKAAN':^40}")
    print("-" * 40)

    # Membuat dictionary buku baru berdasarkan keys dari template
    buku = dict.fromkeys(buku_template.keys())
    buku['judul'] = input("Judul Buku: ")
    buku['penulis'] = input("Penulis: ")
    buku['tahun_terbit'] = int(input("Tahun Terbit: "))
    TAHUN_PINJAM = int(input("Tahun Terakhir Pinjam (YYYY): "))
    BULAN_PINJAM = int(input("Bulan Terakhir Pinjam (1-12): "))
    TANGGAL_PINJAM = int(input("Tanggal Terakhir Pinjam (1-31): "))
    buku['terakhir_pinjam'] = datetime.datetime(TAHUN_PINJAM, BULAN_PINJAM, TANGGAL_PINJAM)
    buku['status'] = input("Status (TERSEDIA / TIDAK): ").upper()

    # Generate KEY acak 6 huruf kapital
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_perpustakaan.update({KEY: buku})

    # Menampilkan tabel daftar buku
    print(f"\n{'KEYS':<8} {'JUDUL BUKU':<20} {'PENULIS':<24} {'TAHUN TERBIT':<13} {'TANGGAL TERAKHIR PINJAM':<24} {'STATUS':<10}")
    print("-" * 102)

    for key in data_perpustakaan:
        JUDUL = data_perpustakaan[key]['judul']
        PENULIS = data_perpustakaan[key]['penulis']
        TAHUN = data_perpustakaan[key]['tahun_terbit']
        PINJAM = data_perpustakaan[key]['terakhir_pinjam'].strftime("%x")
        STATUS = data_perpustakaan[key]['status']

        print(f"{key:<8} {JUDUL:<20} {PENULIS:<24} {TAHUN:<13} {PINJAM:<24} {STATUS:<10}")

    print("\n")
    is_done = input("Mau tambah buku lagi (y/n)? ").lower()
    if is_done == "n":
        break

print("\nAkhir dari program, terima kasih")