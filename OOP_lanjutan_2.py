#  property (Getter & Setter modern)
# biasanya kita akses atribut langsung(obj.atribut), tapi kalau mau mengotrol cara akses, kita bisa menggunakan @property

# @property : membuat method bisa diakses seperti atribut 
# @jari.setter : kontrol saat atribut berubah
# luas dihitung otomatis tanpa dipanggil fungsi

class Lingkaran:
    def __init__(self, jari):
        self._jari = jari
    
    @property
    def jari(self):
        return self._jari
    
    @jari.setter
    def jari(self, nilai):
        if nilai > 0:
            self._jari = nilai
        else:
            print("jari-jari harus positif")
        
    @property
    def luas(self):
        import math
        return math.pi * (self._jari ** 2)

# contoh pemakaian
l = Lingkaran(10)
print(l.luas)
l.jari = -5 # ditolak
l.jari = 7
print(l.luas)

# Static method 
# static method tidak tergantung pada objek atau class.
# biasanya dipakai untuk fungsi utilitas.

class Matematika:
    @staticmethod
    def tambah(a, b):
        return a + b
    
    @staticmethod
    def kali(a, b):
        return a + b

print(Matematika.tambah(5, 3))
print(Matematika.kali(4, 2))

# @staticmethod: bisa dipanggil tanpa buat object (matematika.tambah(...))

# CLass Method
# class method berhubungan dengan class, bukan object
# biasanya dipakai untuk factory method(membuat objek dengan cara khusus)

class Pegawai:
    jumlah_pegawai = 0

    def __init__(self, nama):
        self.nama = nama
        Pegawai.jumlah_pegawai += 1

    @classmethod
    def total_pegawai(cls):
        return f"Total pegawai: {cls.jumlah_pegawai}"
    
# tes
p1 = Pegawai("Budi")
p2 = Pegawai("Andi")
print(Pegawai.total_pegawai())

# @classmethod: parameter pertama cls (bukan self).
# Bisa mengakses atribut milik class, bukan objeck

# Abstract Class
# kalu ada class yang tidak boleh dibuat object langsung, tapi harus diwariskan : gunakan abstract class

from abc import ABC, abstractclassmethod

class Hewan(ABC):
    @abstractclassmethod
    def suara(self):
        pass
class Kucing(Hewan):
    def suara(self):
        return "Meong!"

class Anjing(Hewan):
    def suara(self):
        return "Guk guk!"
    
# h = Hewan() # error, karena abstract
k = Kucing()
print(k.suara())

# ABC : Abstract Base Class
# @abstractmethod: wajib diimplementasikandi subclass.

# Magic Method(__str__, __len__, dll)
# Magic method = method khusus dengan __ di depan dan belakang

class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def __str__(self):
        return f"{self.judul} oleh {self.penulis}"
    
    def __len__(self):
        return len(self.judul)
    
b = Buku("Belajar Python", "Hanif")
print(b)        # panggil __str__
print(len(b))   # panggil __len__

