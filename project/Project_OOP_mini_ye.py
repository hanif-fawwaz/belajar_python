class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self._status = "Tersedia" # default

    @property
    def status(self):
        return self._status
    
    def pinjam(self):
        if self._status == "Tersedia":
            self._status = "Dipinjam"
            return True
        return False
    
    def kembalikan(self):
        self._status = "Tersedia"

    def __str__(self):
        return f"{self.judul} oleh {self.penulis} {self.status}"
    
class Anggota:
    total_anggota = 0

    def __init__(self, nama):
        self.nama = nama
        self.buku_pinjam = []
        Anggota.total_anggota += 1

    def pinjam_buku(self, buku):
        if buku.pinjam():
            self.buku_pinjam.append(buku)
            print(f"{self.nama} meminjam {buku.judul}")
        else:
            print(f"{buku.judul} sedang dipinjam orang lain.")
    
    def kembalikan_buku(self, buku):
        if buku in self.buku_pinjam:
            buku.kembalikan()
            self.buku_pinjam.remove(buku)
            print(f"{self.nama} mengembalikan {buku.judul}")

    @classmethod
    def total(cls):
        return cls.total_anggota
    
    def __str__(self):
        return f"Anggota: {self.nama}, buku dipinjam: {len(self.buku_pinjam)}"
    

class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []
        self.daftar_anggota = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)
    
    def tambah_anggota(self, anggota):
        self.daftar_anggota.append(anggota)

    def daftar_buku_tersedia(self):
        print("\nDaftar Buku Tersedia:")
        for buku in self.daftar_buku:
            if buku.status == "Tersedia":
                print("-", buku)

    def __str__(self):
        return f"Perpustakaan {self.nama} punya {len(self.daftar_buku)} buku dan {len(self.daftar_anggota)} anggota"

# Contoh penggunaan
# Buat perpustakaan
perpus = Perpustakaan("Hanif Library")

# tambah buku
b1 = Buku("Python Dasar", "Guido")
b2 = Buku("Belajar AI", "Andrew Ng")
b3 = Buku("OOP Master", "Hanif")
perpus.tambah_buku(b1)
perpus.tambah_buku(b2)
perpus.tambah_buku(b3)

# Tambah anggota
a1 = Anggota("Budi")
a2 = Anggota("Ani")
perpus.tambah_anggota(a1)
perpus.tambah_anggota(a2)

print(perpus)

# Tambah buku sebelum dipinjam
perpus.daftar_buku_tersedia()

# Pinjam buku
a1.pinjam_buku(b1)
# a2.pinjam_buku(b1) # gagal tiddak bisa dipinjam
a2.pinjam_buku(b2)

# Daftar buku setelah dipinjam
perpus.daftar_buku_tersedia()

# Kembalikan buku
a1.kembalikan_buku(b1)
perpus.daftar_buku_tersedia()

# Total anggota
print("Total anggota:", Anggota.total())