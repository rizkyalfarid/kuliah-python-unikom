def isi_AB():
    # I.S. : Pengguna memasukkan harga A dan Harga B
    # F.S : Menghasilkan harga A dan Harga B
    A = int(input('Masukkan Harga A : '))
    B = int(input('Masukkan Harga B : '))

    # Validasi harga B
    while B < 0:
        print('Harga B tidak boleh negatif, ulangiiiii. Tekan enter!!')
        B = int(input('Masukkan Harga B : '))

    return A, B

def pangkat(A, B):
    # I.S : Harga A dan Harga B sudah terdefinisi
    # F.S : Menghasilkan fungsi A Pangkat B
    if B == 0:
        return 1
    elif B == 1:
        return A
    else:
        pangkat_AB = A
        for i in range(2, B + 1):
            pangkat_AB *= A

        return pangkat_AB

def tampil_pangkat(A, B):
    # I.S. : Harga A dan Harga B sudah terdefinisi
    # F.S : Menampilkan A pangkat B menggunakan operator perkalian
    print(f'{A} Pangkat {B} = ', end='')

    if B > 1:
        for i in range(2, B + 1):
            print(A, end='')
            if i != B:
                print(' x ', end='')

        print('\n              = ', end='')

    print(pangkat(A, B))

# Badan program utama
A, B = isi_AB()
tampil_pangkat(A, B)
