evenNumber = [num for num in range(501) if num % 2 == 0]
nilai = 68 
if nilai>=80:   
    print("Selamat! Anda mendapat nilai A")
elif nilai>=60:
    print("Hmm.. Anda mendapat nilai B")
else:
    print("Waduh, Anda mendapat nilai C")
var_arr = [1, 7, 2, 89, 3]
left_pointer = var_arr[0]
for i in range(1, len(var_arr)):
    right_pointer = var_arr[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer
print(left_pointer)
var_array = [i for i in range(101)] 
total = sum(var_array)
result = total / len(var_array)
def minimal(a, b):
    if a <= b:
        return a
    else:
        return b
result = minimal(10, 5)
print(result)

class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
class Cat(Animal):
    def deskripsi(self):
        return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
    def suara(self):
        return "meow!"
myCat = Cat(name="Neko", age=3, species="Persian")

class Kalkulator:
    def __init__(self, nilai=0):
        self.nilai = nilai
    def tambah_angka(self, angka1, angka2):
        self.nilai = angka1 + angka2
        if self.nilai > 9:             
            print('kalkulator sederhana melebihi batas angka: {}'.format(self.nilai))
        return self.nilai

