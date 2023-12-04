# Memasukkan banyak suku N
N = int(input("Masukkan banyak suku N: "))

# Validasi banyak suku
while N < 1 or N > 20:
    print("Banyak suku harus antara 1-20, ulangi!!")
    # Memasukkan banyak suku kembali
    N = int(input("Masukkan banyak suku N: "))

Suku1 = 0
Suku2 = 1

print("Barisan Fibonacci:")
for i in range(N):
    print(Suku1, end=", ")
    Suku1, Suku2 = Suku2, Suku1 + Suku2
