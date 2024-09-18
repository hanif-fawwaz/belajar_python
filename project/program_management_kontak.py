import function_1

# list of dictionary
daftar_kontak = []

#Menu program
while True:
    print("# Menu")
    print("1.daftar kontak")
    print("2.tambah kontak")
    print("3.hapus kontak")
    print("4.cari kontak")
    print("0.keluar program")

    menu = input("Pilih menu :")

    if menu == "0":
        break
    elif menu == "1":
        function_1.display_kontak(daftar_kontak)
    elif menu == "2":
        kontak = function_1.new_kontak()
        daftar_kontak.append(kontak)
    elif menu == "3":
        function_1.hapus_kontak(daftar_kontak)
    elif menu == "4":
        function_1.cari_kontak(daftar_kontak)
    else:
        print("menu tidak tersedia")

print("Program selesai berjalan,sampai jumpa")