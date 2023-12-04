# MENENTUKAN BILANGAN GENAP ATAU GANJIL 
# I.S : PENGGUNA MEMASUKKAN ANGKA 
# I.F : PROGRAM MENAMPILKAN BILANGAN GENAR ATAU GANJIL

angkaInput = int(input('Masukkan Angka Kamu :'))

# MENGECEK BILANGAN INPUT HABIS DI BAGI 2
if(angkaInput % 2 == 0) :
  print(angkaInput, 'adalah Bilangan genap')
else :
  print(angkaInput, 'adalah Bilangan ganjil')