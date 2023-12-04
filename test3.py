# PROGRAM KONVERSI NILAI
# I.S. PENGGUNA MEMASUKKAN SEBUAH NILAI 
# F.S PROGRAM MENAMPILKAN INDEKS NILAI 

Nilai = int(input('Masukkan Nilai : '))

if(Nilai >= 80 ) and (Nilai <= 100) :
  Indeks = 'A'
elif 70 <= Nilai <= 79 :
  Indeks = 'B'
elif Nilai in range(60,70):
  Indeks = 'C'
elif 50 <= Nilai <= 59:
  Indeks = 'D'
else : 
  Indeks = 'E'

print('Indek Nilai : ', Indeks)
