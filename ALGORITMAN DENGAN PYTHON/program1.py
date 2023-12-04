# PROGRAMPEMBAYARANPEMBELIAN
# {I.S : Program Pembayaran Pembelian}
# {I.F : Program Menampilkan Detail Barang}

KodeBarang = str(input("MasukkN kode Barang : "))

# MENGECEK APAKAH KODE BARANG SESUAI ATAU TIDAK 
if(KodeBarang.upper() == 'SP01') or (KodeBarang.upper() == 'TS02') :
  jumlahBeli = int(input("Jumlah Yang di beli : "))

  if(KodeBarang == 'SP01') :
    NamaBarang = 'Sepatu'
    HargaSatuan = 125000
  else :
    NamaBarang = 'Tas'
    HargaSatuan = 95000

  # MENGHITUNG HARGA TOTAL 
  HargaTotal = HargaSatuan * jumlahBeli

  # MENENTUKAN DISKON
  Diskon = 0
  Potongan = '0%'

  if(KodeBarang.upper() == 'SP01') and (HargaTotal >= 200000) :
    Diskon = 0.125 * HargaTotal
    Potongan = '12.5%'
  TotalBayar = HargaTotal - Diskon

  print()
  print('-' * 30)
  print(f'Kode Barang   : {KodeBarang}')
  print(f'Nama Barang   : {NamaBarang}')
  print(f'Jumlah Beli   : {jumlahBeli}')
  print(f'Harga Satuan  : Rp. {HargaSatuan:10,.0f}')
  print(f'Harga total   : Rp. {HargaTotal:10,.0f}')
  print(f'Potongan {Potongan:5} : Rp. {Diskon:10,.0f}')
  print('-' * 30)
  print(f'Total Bayar : Rp. {TotalBayar:10,.0f}') 
  Bayar = int(input('Bayaran      : Rp. '))
  if(Bayar < TotalBayar) :
    print('Pembayaran Kurang, Tekan Enter!')
    Bayar = int(input('Bayar      : Rp. '))
  Kembalian = Bayar - TotalBayar
  print(f'Uang Kembali    : Rp. {Kembalian:10,.0f}')
else :
  print('Kode Barang Salah')