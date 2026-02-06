# LATIHAN 1: Membuat Class Hero
# Tujuan: Memahami cara membuat class dan atribut instance


class Hero:
    def __init__(self, name, hp, attack_power):
        self.name = name  
        self.hp = hp  
        self.attack_power = attack_power  
    
    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")


hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)

hero1.info()
hero2.info()

print("\n--- Tugas Analisis 1 ---")
hero1.hp = 500
print(f"HP Hero1 setelah diubah: {hero1.hp}")
hero1.info()
