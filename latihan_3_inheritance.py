"""
LATIHAN 3: Pewarisan (Inheritance)
Tujuan: Membuat role khusus (Mage) yang mewarisi sifat Hero tapi punya keunikan
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


# Class Mage adalah anak dari class Hero
class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
        # Memanggil constructor milik Parent (Hero)
        super().__init__(name, hp, attack_power)
        self.mana = mana
    
    def info(self):
        print(f"{self.name} [Mage] | HP: {self.hp} | Mana: {self.mana}")
    
    # Mage punya skill khusus
    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.name} menggunakan Fireball ke {lawan.name}!")
            self.mana -= 20
            lawan.diserang(self.attack_power * 2)  # Damage 2x lipat
        else:
            print(f"{self.name} gagal skill! Mana tidak cukup.")


# -- Main Program --
print("--- Membuat Hero Biasa dan Mage ---")
eudora = Mage("Eudora", 80, 30, 100)
balmond = Hero("Balmond", 200, 10)

eudora.info()
balmond.info()

print("\n--- Pertarungan Dimulai ---")
eudora.serang(balmond)  # Serangan biasa (warisan dari Hero)
print()
eudora.skill_fireball(balmond)  # Skill khusus Mage
print()
balmond.serang(eudora)  # Balmond membalas

print("\n--- Status Akhir ---")
eudora.info()
balmond.info()

print("\n--- Tugas Analisis 3 ---")
print("Coba comment super().__init__() di class Mage untuk melihat error!")
# Jika super() dihapus, atribut name, hp, attack_power tidak akan diinisialisasi
# Error: 'Mage' object has no attribute 'name'
