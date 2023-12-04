while True:
    print("\nMenu Pilihan:")
    print("1. Kalkulator sederhana")
    print("2. Keliling Persegi Panjang")
    print("3. Menyusun Tiga Nama secara menaik")
    print("0. Keluar")

    pilihan = int(input("Masukkan pilihan (0-3): "))

    if pilihan == 1:
        print("Kalkulator Sederhana")
        bilangan1 = int(input("Masukkan bilangan pertama: "))
        bilangan2 = int(input("Masukkan bilangan kedua: "))
        
        print("Hasil Penjumlahan:", bilangan1 + bilangan2)
        print("Hasil Pengurangan:", bilangan1 - bilangan2)
        print("Hasil Perkalian:", bilangan1 * bilangan2)
        
        # Handle pembagian dengan memeriksa apakah bilangan2 tidak sama dengan 0
        if bilangan2 != 0:
            print("Hasil Pembagian:", bilangan1 / bilangan2)
        else:
            print("Error: Pembagian oleh 0")

    elif pilihan == 2:
        print("Keliling Persegi Panjang")
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        
        keliling = 2 * (panjang + lebar)
        print("Keliling Persegi Panjang:", keliling)

    elif pilihan == 3:
        print("Menyusun Tiga Nama secara menaik")
        nama1 = input("Masukkan nama pertama: ")
        nama2 = input("Masukkan nama kedua: ")
        nama3 = input("Masukkan nama ketiga: ")
        
        # Menyusun tiga nama secara menaik tanpa menggunakan array atau sorted
        if nama1 <= nama2 <= nama3:
            print("Nama-nama secara menaik:", nama1, nama2, nama3)
        elif nama1 <= nama3 <= nama2:
            print("Nama-nama secara menaik:", nama1, nama3, nama2)
        elif nama2 <= nama1 <= nama3:
            print("Nama-nama secara menaik:", nama2, nama1, nama3)
        elif nama2 <= nama3 <= nama1:
            print("Nama-nama secara menaik:", nama2, nama3, nama1)
        elif nama3 <= nama1 <= nama2:
            print("Nama-nama secara menaik:", nama3, nama1, nama2)
        elif nama3 <= nama2 <= nama1:
            print("Nama-nama secara menaik:", nama3, nama2, nama1)

    elif pilihan == 0:
        print("Program selesai. Sampai jumpa!")
        break

    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
