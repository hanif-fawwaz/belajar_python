# Attribute : variabel yang disimpan didalam object

# class Mahasiswa:
#     def __init__(self, nama, umur):
#         self.nama = nama # Attribute
#         self.umur = umur
# m1 = Mahasiswa("Hanif Arib", 18)

# print(m1.nama)
# print(m1.umur)

# Method: fungsi yang ada di dalam class
class  Mahasiswa:
    def __init__(self, nama, umur):
        self.nama = nama # Attribute
        self.umur = umur

    def sapa(self):
        print(f"Halo, saya {self.nama}, umur saya {self.umur}")
m1 = Mahasiswa("Hanif", 18)
m1.sapa() # Halo, saya Hanif, umur saya 18

# Penting: semua method harus punya self sebagai parameter utama

# Method dengan Parameter
class Kalkulator:
    def tambah(self, a, b):
        return a + b
    
k = Kalkulator()
print(k.tambah(5, 3)) # 8