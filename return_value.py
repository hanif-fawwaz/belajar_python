def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    return (list_angka, total)

list_angka, total = jumlahkan(100, 2000)

print(f"total {list_angka} = {total}")