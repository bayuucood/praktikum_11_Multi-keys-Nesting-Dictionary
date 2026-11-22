# LATIHAN 
import datetime
import os
import string
import random

perpus_template = {
    "judul": 'judul',
    "penulis": 'penulis',
    "tahun": 0,
    "tglpinjam": datetime.datetime(1111, 1, 11),
    "status": 'TERSEDIA'  # <-- Tambahan sesuai soal
}

data_perpus = {}

while True:
    # Gunakan "cls" jika di Windows, "clear" jika di Mac/Linux
    os.system("cls" if os.name == "nt" else "clear") 
    
    print("-" * 30)
    print(f"{'Selamat Datang Di Perpustakaan':^30}")
    print(f"{'Masukkan Data Buku':^30}")
    print("-" * 30)

    buku = dict.fromkeys(perpus_template.keys())
    buku['judul'] = input("Masukkan Judul Buku          : ")
    buku['penulis'] = input("Masukkan Penulis Buku        : ")
    buku['tahun'] = int(input("Masukkan Tahun Terbit        : "))
    
    TAHUN_PINJAM = int(input("Tahun Pinjam (YYYY)          : "))
    BULAN_PINJAM = int(input("Bulan Pinjam (1-12)          : "))
    TANGGAL_PINJAM = int(input("Tanggal Pinjam (1-31)        : "))
    buku['tglpinjam'] = datetime.datetime(TAHUN_PINJAM, BULAN_PINJAM, TANGGAL_PINJAM)
    
    # Tambahan input status
    buku['status'] = input("Status (TERSEDIA/TIDAK)      : ").upper()

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_perpus.update({KEY: buku})

    print(f"\n{'KEY':<8} {'Judul':<22} {'Penulis':<18} {'Tahun':<8} {'Tgl Pinjam':<12} {'Status':<10}")
    print('-' * 82)

    for key in data_perpus:
        KEY = key
        JUDUL = data_perpus[KEY]['judul']
        PENULIS = data_perpus[KEY]['penulis']
        TAHUN = data_perpus[KEY]['tahun']
        TGL = data_perpus[KEY]['tglpinjam'].strftime("%x")
        STATUS = data_perpus[KEY]['status']
        
        print(f"{KEY:<8} {JUDUL:<22} {PENULIS:<18} {TAHUN:<8} {TGL:<12} {STATUS:<10}")
    print("\n")

    is_done = input("Apakah anda ingin menambahkan buku lagi? (y/n) : ").lower()
    if is_done == "n":
        print("\nTerima kasih!!!!!")
        break