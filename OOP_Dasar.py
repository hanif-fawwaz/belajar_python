# Apa itu OOP?
# Object-Oriented Programing (OOP) adalah cara menulis program dengan:

# - Class : Cetakan/Bentuk
# - Object : Barang nyata dari cetakan
# Contoh : class Mahasiswa, object-nya: Hanif, Adit

# Membuat Class dan Object
class Mahasiswa:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

m1 = Mahasiswa("Hanif", 18)

print(m1.nama) # Hanif
print(m1.umur) # 18

# __init__() adalah fungsi khusus yang dijalakan saat objek dibuat

# Penjelasan self
# self mempresentasikan object itu sendiri saat dibuat
# Contoh: m1.nama itu sama dengan self.nama dalam class
