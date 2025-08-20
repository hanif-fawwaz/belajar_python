# Fungsi dengan nilai Default

def sapa(nama ="Teman"):
    print(f"Halo, {nama}!")
sapa()
sapa("Hanif")

# Fungsi dengan return
def tambah(a, b):
    return a+ b

hasil = tambah(6, 4)
print(f"Hasil: {hasil}")

# Fungsi Anonymous (Lambda)
kali = lambda x,y: x*y
print(kali(5, 2))

# Cocok untuk fungsi kecil & cepat, misal sorting:

data = [("A", 2), ("B", 1)]
data.sort(key=lambda x: x[1])
print(data) # [('B', 1), ('A', 2)]

# Scope (Lingkup Variabel)

x = 5
def ubah():
    x = 10
    print(f"Dalam fungsi: {x}")

ubah()
print(f"Di luar fungsi: {x}")

# Hasil:
# Dalam fungsi: 10
# Di luar fungsi: 5

# Untuk ubah variabel global didalam fungsi:
def ubah():
    global x
    x = 10