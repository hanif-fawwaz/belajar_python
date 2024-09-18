def say_hallo(nama):
    return f"Hello {nama}"

def total(*list_angka):
    hasil = 0
    for hasil in list_angka:
        hasil = hasil + hasil
    return hasil