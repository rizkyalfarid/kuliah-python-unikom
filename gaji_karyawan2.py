# Program penggajian karyawan
# I.S. Pengguna memasukkan bulan dan tahun penggajian Nomor Induk Karyawan (NIK), nama karyawan (Nama)
#      Golongan (Gol), jumlah anak (Anak), Jumlah jam kerja perbulan (JamKerja)
# F.S. Program menampilkan data karyawan berserta gaji yang sudah dihitung

# input data pengguna
Bulan = str(input('Masukkan Bulan             : '))
Tahun = str(input('Masukkan Tahun             : '))
NIK = str(input('Masukkan Nomor NIK         : '))
Nama = str(input('Masukkan Nama Karyawan     : '))
Gol = int(input('Masukkan Golongan Karyawan : '))

# validasi golongan
if (Gol < 1) or (Gol > 4) :
    print('Gologngan hanya boleh diisi 1/2/3/4')
else :
    # memasukkan jumlah anak dan jumlah jam kerja
    Anak = int(input('Masukkan Jumlah Anak       : '))
    JamKerja = int(input('Masukkan Jumlah Jam Kerja  : ')) 
    
    # menentukan gaji pokok dan tunjangan
    match Gol :
        case 1 :
            GajiPokok = 1750000
            BesarTunjangan = '12.5%'
            Tunjangan = 0.125 * GajiPokok
        case 2 :
            GajiPokok = 2300000
            BesarTunjangan = '15%'
            Tunjangan = 0.15 * GajiPokok
        case 3 :
            GajiPokok = 3250000
            BesarTunjangan = '17.5%'
            Tunjangan = 0.175 * GajiPokok
        case 4 :
            GajiPokok = 3600000
            BesarTunjangan = '17.5%'
            Tunjangan = 0.175 * GajiPokok
    
    # menentukan tunjangan anak
    if Anak > 2 :
        TunjanganAnak = 300000
    else :
        TunjanganAnak = Anak * 150000

    # menghitung jam lembur dan uang lembur
    JamLembur = 0
    Lembur = 0
    if JamKerja > 200 :
        JamLembur = JamKerja - 200
        Lembur = JamLembur * 250000
    
    # menghitung jam kurang dan potongan
    Potongan = 0
    if JamKerja < 200 :
        JamKurang = 200 - JamKerja
        if JamKurang >= 8 :
            Hari = JamKurang // 8
            Sisa = JamKurang % 8
            Potongan = Hari * 50000 + Sisa * 10000
        else :
            Potongan = JamKurang * 10000

    # menghitung gaji bersih karyawan
    GajiBersih = GajiPokok + Tunjangan + TunjanganAnak + Lembur - Potongan

    # output data karyawan dan hasil hitung gaji
    print()
    print('               SLIP GAJI')
    print('               ---------')
    print(f'Bulan : {Bulan:10} Tahun : {Tahun}')
    print(f'NIK   : {NIK:10} Nama  : {Nama}')
    print('-'*40)
    print(f'Golongan                : {Gol}')
    print(f'Jumlah Anak             : {Anak}')
    print(f'Jumlah Jam Kerja/Bulan  : {JamKerja}')
    print(f'Gaji Pokok              : Rp. {GajiPokok:10,.0f}')
    print(f'Tunjangan {BesarTunjangan:9} : Rp. {Tunjangan:10,.0f}')
    if(JamLembur != 0) :
        print()
        rpnit
    else :
        print()