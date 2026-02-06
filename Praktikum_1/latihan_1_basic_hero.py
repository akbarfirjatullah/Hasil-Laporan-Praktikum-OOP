"""
LATIHAN 1: Membuat Class Hero
Tujuan: Memahami cara membuat class dan atribut instance
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


# -- Main Program --
# Membuat Object (Instansiasi)
hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)

# Memanggil Method
hero1.info()
hero2.info()

print("\n--- Tugas Analisis 1 ---")
# Mengubah HP hero1 setelah dibuat
hero1.hp = 500
print(f"HP Hero1 setelah diubah: {hero1.hp}")
hero1.info()
