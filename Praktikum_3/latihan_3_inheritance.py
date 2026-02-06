# LATIHAN 3: Pewarisan (Inheritance)
# Tujuan: Membuat role khusus (Mage) yang mewarisi sifat Hero tapi punya keunikan

class Hero:
    def __init__(self, name, hp, attack_power):
        self.name = name 
        self.hp = hp 
        self.attack_power = attack_power 
    
    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")
    
    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)
    
    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")


class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp, attack_power)
        self.mana = mana
    
    def info(self):
        print(f"{self.name} [Mage] | HP: {self.hp} | Mana: {self.mana}")
    
    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.name} menggunakan Fireball ke {lawan.name}!")
            self.mana -= 20
            lawan.diserang(self.attack_power * 2)  
        else:
            print(f"{self.name} gagal skill! Mana tidak cukup.")


print("--- Membuat Hero Biasa dan Mage ---")
eudora = Mage("Eudora", 80, 30, 100)
balmond = Hero("Balmond", 200, 10)

eudora.info()
balmond.info()

print("\n--- Pertarungan Dimulai ---")
eudora.serang(balmond) 
print()
eudora.skill_fireball(balmond) 
print()
balmond.serang(eudora) 

print("\n--- Status Akhir ---")
eudora.info()
balmond.info()

print("\n--- Tugas Analisis 3 ---")
print("Coba comment super().__init__() di class Mage untuk melihat error!")
