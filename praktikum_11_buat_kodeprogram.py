# PROGRAM 11.1 MULTI KEYS & NESTING DICTIONARY
import datetime
mahasiswa1 = {
    'nama': 'bayu bayem',
    'nim': '2605060024',
    'sks_lulus': 130,
    'beasiswa' : False,
    'lahir' : datetime.datetime (2008, 2 ,2) # tahun, bulan, tanggal
}

mahasiswa2 = {
    'nama': 'nico robin',
    'nim': '2605060026',
    'sks_lulus': '140',
    'beasiswa' : 'True',
    'lahir' : datetime.datetime (2002, 3 ,3) # tahun, bulan, tanggal
}

mahasiswa3 = {
    'nama': 'tony choper',
    'nim': '2605060027',
    'sks_lulus': '100',
    'beasiswa' : 'True',
    'lahir' : datetime.datetime (1999, 10 ,5) # tahun, bulan, tanggal
}

data_mahasiswa = {
    'MAH001' : mahasiswa1,
    'MAH002' : mahasiswa2,
    'MAH003' : mahasiswa3
}

print (f"('KEY':<6) {'NAMA':<6} {'SKS':<3} {'BEASISWA':<9} {'LAHIR':<10}")
print ("-"*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa [KEY] ['nama']
    NIM = data_mahasiswa [KEY] ['nim']
    SKS = data_mahasiswa [KEY] ['sks_lulus']
    BEASISWA = data_mahasiswa [KEY] ['beasiswa']
    LAHIR = data_mahasiswa [KEY] ['lahir'].strftime ("%x")

    print (f"{KEY: <6} {NAMA: <17} {SKS: <3} {BEASISWA!s: <9} {LAHIR: <10}")
    print ()

# program 11.2
import datetime

mahasiswa_template = {
    'nama': 'nama',
    'nim': 'nim',
    'sks_lulus': 0,
    'lahir': datetime.datetime(1111, 1, 1)
}

data_mahasiswa = {}

print(f"{'SELAMAT DATANG GUYS':^20}")
print(f"{'DATA MAHASISWA UNTID':^20}")
print("-" * 20)

mahasiswa = dict.fromkeys(mahasiswa_template.keys())
print(mahasiswa)

mahasiswa['nama'] = input("Nama Mahasiswa: ")
mahasiswa['nim'] = input("NIM Mahasiswa: ")
mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))

TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))

mahasiswa['lahir'] = datetime.datetime(
    TAHUN_LAHIR,
    BULAN_LAHIR,
    TANGGAL_LAHIR
)

print(mahasiswa)
print ()

# program 11.3
import datetime
import os
import string
import random

# template dict mahasiswa
mahasiswa_template = {
    'nama':'nama',
    'nim':'00000000',
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

while True:
    # os.system("cls") # untuk windows
    os.system("clear")
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input("Nama Mahasiswa: ")
    mahasiswa['nim'] = input("NIM Mahasiswa: ")
    mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
    TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
    BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
    TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))
    mahasiswa['lahir'] =datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in
range(6)))
    data_mahasiswa.update({KEY:mahasiswa})

    # dari program sebelumnya, hilangkan beasiswa
    print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<8} {'SKS Lulus':<10} {'Tanggal Lahir':<10}")
    print('-'*60)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
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