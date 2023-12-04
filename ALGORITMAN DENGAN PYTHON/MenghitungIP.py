# # MenghitungIndeksPrestasi 
# # I.S. : Pengguna memasukkan NIM, Nama, Semester, TIga Matakuliah, SKS

# # F.s Program Menampilkan Indeks Prestasi(IP)

# # Const 
# NILAI1 = 'B'
# NILAI2 = 'D'
# NILAI3 = 'C'
# BOBOT1 = 3
# BOBOT2 = 1
# BOBOT3 = 2

# # Input 
# NIM =      str(input('Masukkan NIM                  : '))
# Nama =     str(input('Masukkan Nama                 : '))
# Kelas =    str(input('Masukkan Kelas                : '))
# Semester = str(input("Masukkan Semester             : "))

# # Input Mata Kuliah 

# Matkul_1 = str(input("Masukkan Matkul 1             : "))
# SKS_1 = int(input('Masukkan Jumlah SKS Matkul 1     : '))

# Matkul_2 = str(input("Masukkan Matkul 2             : "))
# SKS_2 = int(input('Masukkan Jumlah SKS Matkul 2     : '))

# Matkul_3 = str(input("Masukkan Matkul 3             : "))
# SKS_3 = int(input('Masukkan Jumlah SKS Matkul 3     : '))

# # Proses
# TotalNilai = (SKS_1 * BOBOT1) + (SKS_2 * BOBOT2) + (SKS_3 * BOBOT3)
# TotalSKS = SKS_1 + SKS_2 + SKS_3
# ip = TotalNilai / TotalSKS

# # Output
# print('Kartu Hasil Studi')
# print('NIM    :', NIM)
# print('Nama    :', Nama)
# print('Kelas    :', Kelas)
# print('Semester    :', Semester)

# H_Matkul = "Nama Mata Kuliah"
# print(f'| {H_Matkul:30} |  SKS  |  Nilai  |')
# print(f'| {Matkul_1:30} | {SKS_1:5} | {NILAI1:7} |')
# print(f'| {Matkul_2:30} | {SKS_2:5} | {NILAI2:7} |')
# print(f'| {Matkul_3:30} | {SKS_3:5} | {NILAI3:7} |')

# print(f'IP : {ip:5.2f}')

# LATIHAN SOAL 2

# MENGONVERSIKAN DURASI WAKTU 
# I.S. : User Memasukkan Detik(Jumlahdetik) 
# F.S. : Menampilkan Hari, Jam, Menit, Detik

# Menentukan Hari
DetikInput = int(input("Masukkan Detik :"))
hari = DetikInput // 86400
sisaDetik = DetikInput % 86400

# Menentukan Jam
jam = sisaDetik // 3600
sisaDetik = sisaDetik % 3600

# Menentukan Menit dan Detik
menit = sisaDetik // 60
detik = sisaDetik % 60

# Output
print(DetikInput, 'Detik Adalah : ', hari, 'Hari,', jam, 'Jam,', menit, 'Menit,', detik, 'Detik')


