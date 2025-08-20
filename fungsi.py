# Fungsi Sederhana
def sapa():
    print("Halo! Selamat datang!")
sapa()

# Fungsi dengan Parameter
def sapa_nama(nama):
    print(f"Halo, {nama}")

sapa_nama("Hanif")

# Fungsi dengan return
def jumlah(a, b):
    return a + b
hasil = jumlah(5,1)
print(f"Jumlahnya adalah {hasil}")

# Scope Variable (lokal vs global)

x = 10
def ubah():
    x = 5
    print(f"Di dalam fungsi: {x}")

ubah()
print(f"Di luar fungsi: {x}")

# Default Parameter & Argumen Opsional
def sapa(nama="Teman"):
    print(f"Hai {nama}")
sapa() # Hai Teman
sapa("Hanif") # Hai Hanif

