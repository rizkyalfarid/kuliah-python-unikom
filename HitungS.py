#PROGRAM HITUNG S
'''
{I.S : Pengguna Memasukkan Banyak suku (n)}
{F.S : menampilkan hasil perhitungan s = -1/2 + 4/6 = 18/21 + ..'}
'''

import os;
# memasukkan banyak suku
N = int(input('Banyak Suku yang akan di hitung : '))

# validasi banyak suku
while ( N < 1) or (N > 10) :
  print('Banyak suku harus antara 1 - 10, ulangi!')
  os.system('pause')
  os.system('cls')
  N = int(input('Banyak Suku yang akan di hitung : '))

# menghitung S
S = 0
Pembilang = 1
Penyebut = 1

print(f'S =', end='')
for i in range(N):
  i = i + 1
  Pembilang = Penyebut * i
  Penyebut = Pembilang + i
  if(i % 2 == 1) :
    print(f' - {Pembilang:0.0f}/{Penyebut}',end='')
    S = S - Pembilang/Penyebut
  else :
    print(f' + {Pembilang:0.0f}/{Penyebut}',end='')
    S = S + Pembilang/Penyebut

#menampilkan harga s
print() 
print(f' = {S:0.3f}')
    
