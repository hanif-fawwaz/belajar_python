class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
    
    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Jurusan: {self.jurusan}")
    
class ManajemenMahasiswa:
    def __init__(self):
        self.daftar_mahasiswa = []

    def tambah_mahasiswa(self, mhs):
        self.daftar_mahasiswa.append(mhs)
    
    def hapus_mahasiswa(self, mhs):
        # data_ditemukan1 = None
        # print("1. menghapus satu data")
        # print("2. Hapus seluruh data")
        # pilihan_2 = input("Masukan nomor: ")
        # if pilihan_2 == "1":    
        #     pilih_nama = input("Masukan nama: ")
        #     for pengguna in self.daftar_mahasiswa:
        #         if pengguna['nama'] == pilih_nama:
        #             print("Data Mahasiswa ditemukan")
        #             data_ditemukan1 = pengguna
        #         else:
        #             break
        #     if data_ditemukan1:
        #         self.daftar_mahasiswa.remove(data_ditemukan1)
        #         print("Data berhasil dihapus")
        # if pilihan_2 == "2":
        #     self.daftar_mahasiswa.clear()
        #     print("Data berhasil dihapus")
        self.daftar_mahasiswa.remove(mhs)
    
    def tampilkan_semua(self):
        print("=== Daftar Mahasiswa ===")
        for mhs in self.daftar_mahasiswa:
            mhs.tampilkan_info()
            print("-" * 20)
        # if len(self.daftar_mahasiswa) == 0:
        #     print("Belum ada data.")
        # else:
        #     for mhs in enumerate(self.daftar_mahasiswa):
        #         mhs.tampilkan_info()

    def cari_by_nim(self, nim):
        for mhs in self.daftar_mahasiswa:
            if mhs == nim:
                print("Data Ditemukan")
                mhs.tampilkan_info()
                return
        
            print("Mahasiswa dengan NIM tersebut tidak ditemukan")
    
    def jumlah_total(self):
        print(f"Total Mahasiswa: {len(self.daftar_mahasiswa)}")

# membuat objek sistem manajemen
sistem = ManajemenMahasiswa()

# Menambahkan mahasiswa
sistem.tambah_mahasiswa(Mahasiswa("Alya", 22001, "Informatika"))
sistem.tambah_mahasiswa(Mahasiswa("Budi", 22002, "Teknik Elektro"))
sistem.tambah_mahasiswa(Mahasiswa("Citra", 22003, "Sistem Informasi"))

# Menampilkan semua mahasiswa
sistem.tampilkan_semua()

# Mencari mahasiswa berdasarkan NIM
sistem.cari_by_nim(22002)

# Menampilkan total mahasiswa
sistem.jumlah_total()

# Program utama (menu)
# while True:
#     print("=== MENU ===")
#     print("1. Tambah Data Mahasiswa")
#     print("2. Lihat Semua Data")
#     print("3. Cari Mahasiswa")
#     print("4. Hapus Mahasiswa")
#     print("5. Keluar")
#     print("============")
#     pilihan = input("Pilih menu: ")

#     if pilihan == "1":
        
#     elif pilihan == "2":
        
#     elif pilihan == "3":
        
#     elif pilihan == "4":
        
#     elif pilihan == "5":
#         print("Terima Kasih! Program selesai.")
#         break
#     else:
#         print("Pilihan tidak valid!\n")