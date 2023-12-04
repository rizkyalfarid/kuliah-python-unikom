# Program ini akan menghitung upah mingguan seorang karyawan
# I.S: Karyawan memasukkan jam kerja per minggu
# F.S: Menampilkan upah karyawan per minggu

# Meminta input dari pengguna
namaKaryawan = input('Masukkan Nama Karyawan: ')
posisiPekerjaan = input('Masukkan Posisi Pekerjaan: ')
jamKerja = int(input('Masukkan jam kerja per minggu: '))
upahPerJam = int(input('Masukkan upah per jam (Rp.): '))

# Pengecekan jam kerja apakah lebih dari 40 jam atau tidak
# Menghitung upah
if (jamKerja > 40):
    upahMingguan = jamKerja * upahPerJam * 2
    keteranganUpah = 'Upah lembur'
else:
    upahMingguan = jamKerja * upahPerJam
    keteranganUpah = 'Upah tidak lembur'

# Menampilkan hasil
print(f"{keteranganUpah} mingguan untuk {namaKaryawan} sebagai {posisiPekerjaan} adalah: Rp. {upahMingguan}")
