'''
Program Volume Kubus 
{I.S Pengguna Memasukkan Sisi Kubus}
{F.S Program Menampilkan Volume Kubus}
'''

# Interger = Int, real = float, string/char = str
Sisi = int(input('Masukkan Sisi Kubus :'))
Volume = Sisi**3 / 1000000

# Output (Volume)
print("Volume Kubus :",Volume,'cm')
print(f'Volume Kubus:{Volume:10,}cm')
