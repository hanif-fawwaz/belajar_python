customer = {"name":"hanif", "umur":"17", "asal":"Brebes"}

name = customer["name"]
umur = customer["umur"]
asal = customer["asal"]

customer["company"] = "x" #untuk menambahkan
customer["name"] = "Hanif Arib Fawwaz"

del customer["asal"]#untuk menghapus

for key, value in customer.items():
    print(f"{key}:{value} ")

