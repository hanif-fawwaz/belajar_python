# [] = list
# () = tuple (tidak bisa di tambahkan)
# {} = set (acak) , (unik)

nama = {"hanif", "zufar", "razin"}

nama.add("aira")
nama.add("razin")
nama.add("razin")

for name in nama:
    print(name)

nama.remove("hanif")
nama.remove("zufar")

print(nama)