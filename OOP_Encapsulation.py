# Encapsulation: Membatasi akses langsung ke data (atribut) agar tidak sembarangan diubah dari luar
# Privat Attribute(__nama_variabel)
# Gunakan double underscore__ untuk menjadikan private:
class Mahasiswa:
    def __init__(self, nama, umur):
        self.__nama = nama # Private
        self.__umur = umur
    
    def tampilkan_data(self):
        print(f"Nama: {self.__nama}, umur {self.__umur}")

# Tidak dapat diakses langsung
# Contoh:
m1 = Mahasiswa("Hanif", 18)
print(m1.__nama) # eror

# Getter: untuk mengambil nilai
def get_nama(self):
    return self.__nama

# Sentter: unutk mengubah nilai
def set_nama(self, nama_baru):
    self.__nama = nama_baru

# Contoh lengkap:
class Mahasiswa:
    def __init__(self, nama, umur):
        self.__nama = nama
        self.__umur = umur
    
    # Getter: untuk mengambil nilai
    def get_nama(self):
        return self.__nama

    # Sentter: unutk mengubah nilai
    def set_nama(self, nama_baru):
        self.__nama = nama_baru


m1 = Mahasiswa("Hanif", 18)
print(m1.get_nama())

m1.set_nama("Adit")
print(m1.get_nama())