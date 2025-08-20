# Inharitance: memungkinkan satu class mewarisi atribut dan method class lain.
# Contoh:
# - class Manusia bisa mewarisi oleh Mahasiswa
# - Mahasiswa otomatis punya atribut, nama, umur dari mahasiswa
# COntoh:
class Manusia:
    def __init__(self, nama):
        self.nama = nama

    def sapa(self):
        print(f"Halo, saya {self.nama}")
    
class Mahasiswa(Manusia):
    def belajar(self):
        print(f"{self.nama} sedang belajar")
m1 = Mahasiswa("Hanif")
m1.sapa() # dari class induk
m1.belajar() # dari class anak

# Override __init__(jika perlu)
class Mahasiswa(Manusia):
    def __init__(self, nama, nim):
        super().__init__(nama) # panggil input init() dari parent
        self.nim = nim

    def info(self):
        print(f"{self.nama} dengan NIM {self.nim}")

# Fungsi super: untuk memgakses method dari parebt class, biasanya digunakan di __init__() atau method lain


