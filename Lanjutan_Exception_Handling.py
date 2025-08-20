# Menangani eror (Exception handling)

'''
Di dunia nyata (dan coding), eror pasti terjadi
python punya cara menangani error supaya program
tidak langsung crash, yaitu dengan try-except.
'''

# Tanpa Handling
x = int(input("masukan angka: "))
hasil = 10 / x
print(f"Hasil: {hasil}")

# Jika dimasukan 0 akan error: ZeroDivisionError

# Dengan Try-Except
try:
    x = int(input("Masukan angka: "))
    hasil = 10 / x
    print(f"Hasil: {hasil}")
except ZeroDivisionError:
    print("Error: Tidak bisa dibagi 0")
except ValueError:
    print("Error: Masukan harus angka!")

# Fungsi try-except: menangkap kesalahan yang terjadi dan menanganinya dengan aman

# Finaly dan else
try:
    angka =int(input("Angka: "))
except ValueError:
    print("Input Salah")
else:
    print(f"Angka berhasil dibaca {angka}")
finally:
    print("Program selesai")
