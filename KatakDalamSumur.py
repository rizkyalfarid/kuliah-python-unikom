import os

# KONSTANTAN NAMA PENGGUNA
PENGGUNA = 'Rizky'
SANDI = '10123028'

# Memasukkan nama pengguna dan kata sandi
print('<< L O G I N >>')
NamaPengguna = str(input('Nama Pengguna :'))
Katasandi = str(input('Katasandi :'))

# Verifikasi login
Ulang = 1
while (NamaPengguna != PENGGUNA or Katasandi != SANDI) and Ulang < 3:
    print('Login Gagal, Ulangi!')
    os.system('pause')
    os.system('cls')

    print('<< L O G I N >>')
    NamaPengguna = str(input('Nama Pengguna :'))
    Katasandi = str(input('Katasandi :'))
    Ulang = Ulang + 1

# Jika login valid
if NamaPengguna == PENGGUNA and Katasandi == SANDI:
    os.system('cls')
    print('<< Menghitung Jumlah Hari Katak Keluar Dari Sumur >>')

    DalamSumur = float(input('Masukkan Jumlah (meter) : '))
    KedalamanSaatIni = 0
    hari = 0

    while KedalamanSaatIni < DalamSumur:
        hari += 1
        if hari <= 3:
            KedalamanSaatIni += 2.5 - 0.5 * (hari % 2)
        elif hari <= 10:
            KedalamanSaatIni += 1.75 - 1 * (hari % 2)
        else:
            KedalamanSaatIni += 1.5 - 0.75 * (hari % 2)

    print(f"\nKatak dapat keluar dari sumur dalam {hari + 1} hari.")

elif Ulang >= 3:
    os.system('cls')
    print('Maaf, sudah gagal 3 kali login. Program berhenti.')
