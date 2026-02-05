"""
LATIHAN 2: Interaksi Antar Objek (Method)
Tujuan: Membuat objek saling berinteraksi (saling serang)
"""

class Hero:
    # Constructor: Dijalankan saat Hero baru dibuat
    def __init__(self, name, hp, attack_power):
        self.name = name  # Nama Hero
        self.hp = hp  # Nyawa (Health Point)
        self.attack_power = attack_power  # Kekuatan Serangan
    
    # Method untuk menampilkan info hero
    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")
    
    # Method menyerang: Objek ini (self) menyerang objek lain (lawan)
    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)
    
    # Method diserang: Menerima damage
    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")


# -- Main Program --
# Membuat Object (Instansiasi)
hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)

# Memanggil Method
hero1.info()
hero2.info()

print("\n--- Pertarungan Dimulai ---")
hero1.serang(hero2)  # Layla menyerang Zilong
hero2.serang(hero1)  # Zilong membalas

print("\n--- Status Setelah Pertarungan ---")
hero1.info()
hero2.info()
