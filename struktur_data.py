# List seperti array
buah = ["apel", "jeruk", "mangga"]
print(buah[0]) # apel
buah.append("nanas")    # tambah
buah.remove("jeruk")    # hapus
print(buah)             # ['apel', 'mangga', 'nanas']

# Tuple list yang tidak bisa diubah
angka = (1,2,3)
print(angka[2])    # 2
# angka[0] = 10    # eror

# Set Data unik, tanpa indeks
angka = {1, 2, 3, 3, 2}
print(angka)    # {1, 2, 3}
angka.add(4)    # tambah
angka.discard(2)# hapus
print(angka)    # {1, 3, 4}

# Dictionary(dict) key dan value
mhs = {"nama": "Hanif", "umur": 18}
print(mhs["nama"])  # Hanif
mhs["jurusan"] = "Informatika" # tambah
print(mhs) # {'nama': 'Hanif', 'umur': 17, 'jurusan': 'Informatika'}