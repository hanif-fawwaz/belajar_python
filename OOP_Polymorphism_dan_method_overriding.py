# Pilymorphism: satu fungsi bisa memiliki bentuk yang berbeda tergantung class-nya
# Contoh:
class Kucing:
    def suara():
        print("Meong")
class Anjing:
    def suara():
        print("Guk guk")

def bunyikan(hewan):
    hewan.suara()

k = Kucing()
a = Anjing()

bunyikan(k) # Meong
bunyikan(a) # Guk guk

# Method Overriding
# Menthod dari class induk ditimpa di class anak
class Kendaraan:
    def suara(self):
        print("Bunyi kendaraan")
    
class Mobil(Kendaraan):
    def suara(self):
        print("Vroom vroom") #Override

m = Mobil()
m.suara() # Vroom vroom
