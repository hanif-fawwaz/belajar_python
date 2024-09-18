def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    print(f"total {list_angka} = {total}")

jumlahkan(12, 13)