# DIBUAT OLEH BERRY RIZKY (10123032) & YOEL BENNY (10123016)

# Input data awal
kecepatan_awal = 5
waktu_awal = 0

# Waktu berangkat
jam_awal = 9
menit_awal = 0
detik_awal = 5

# Waktu sampai
jam_akhir = 13
menit_akhir = 15
detik_akhir = 0

# Konversi waktu ke menit
waktu_awal = waktu_awal + jam_awal * 60 + menit_awal + detik_awal / 60
waktu_akhir = jam_akhir * 60 + menit_akhir + detik_akhir / 60

# Inisialisasi variabel
kecepatan = kecepatan_awal
waktu_tempuh = 0
jarak_tempuh = 0

# Perhitungan waktu tempuh dan jarak tempuh
while waktu_tempuh < waktu_akhir:
    jarak_tempuh += kecepatan / 60
    waktu_tempuh += 10
    kecepatan += 1

# Output hasil
print('Waktu tempuh:', '{:.2f}'.format(waktu_tempuh), 'menit')
print('Jarak tempuh:', '{:.2f}'.format(jarak_tempuh), 'meter')
