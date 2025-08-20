# List Comprehesion (Cara Singkat Membuat list)
# Dari ini:
angka = []
for i in range(5):
    angka.append(i)
print(angka) # [0, 1, 2, 3, 4]

# kita bisa tulis
angka = [i for i in range(5)]
print(angka)

# Bisa juga dengan kondisi:
genap = [i for i in range(10) if i % 2 == 0]
print(genap)

# Nested List
# Contoh Matriks 2D
matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriks[1][2]) # 6

# Sort dan Reserse
angka = [5, 1, 9, 3]
angka.sort()
print(angka) # [1, 3, 5, 9]

angka.sort(reverse=True)
print(angka) # [9, 5, 3, 1]

# membalikan urutan
huruf = ['a', 'b', 'c']
huruf.reserve()
print(huruf) # ['c', 'b', 'a']

# Unpacking LIst (Membongkar isi list)
data = [10, 20, 30]
a, b, c = data
print(a, b, c) # 10 20 30

# Operasi lanjutan pada list
angka = [1, 2, 3]
print(angka * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(angka + [4, 5]) # [1, 2, 3, 4, 5]
