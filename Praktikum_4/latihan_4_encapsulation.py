#LATIHAN 4: Enkapsulasi (Mengamankan Data HP)
# Tujuan: Mencegah HP diubah sembarangan (misal jadi negatif atau di-cheat jadi 9999)


class Hero:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        self.__hp = hp_awal
    
    def get_hp(self):
        return self.__hp
    
    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0  
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000 saja.")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru
    
    def diserang(self, damage):
        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)
        print(f"{self.nama} terkena damage {damage}. Sisa HP: {self.get_hp()}")



print("--- Membuat Hero dengan HP 100 ---")
hero1 = Hero("Layla", 100)
print(f"HP Layla: {hero1.get_hp()}")

print("\n--- Mencoba set HP negatif ---")
hero1.set_hp(-50)  
print(f"HP Layla setelah set -50: {hero1.get_hp()}") 

print("\n--- Mencoba cheat HP 9999 ---")
hero1.set_hp(9999)
print(f"HP Layla setelah cheat: {hero1.get_hp()}")

print("\n--- Reset HP ke 150 ---")
hero1.set_hp(150)
print(f"HP Layla: {hero1.get_hp()}")

print("\n--- Diserang 30 damage ---")
hero1.diserang(30)

print("\n--- Diserang 200 damage (lebih dari HP) ---")
hero1.diserang(200)

print("\n=== TUGAS ANALISIS 4 ===")
print("\n1. Percobaan Hacking dengan Name Mangling:")
print(f"Mencoba akses paksa: {hero1._Hero__hp}")
print("^ Ini berhasil karena Python menggunakan Name Mangling.")
print("  Tapi ini TIDAK BOLEH dilakukan dalam praktik yang baik!")

print("\n2. Uji Validasi (commented out untuk keamanan):")
print("   Jika logika if/elif di setter dihapus, HP bisa jadi negatif!")
print("   Ini berbahaya untuk integritas data game.")

# Demonstrasi bahaya tanpa validasi (di-comment untuk keamanan)
"""
class HeroTanpaValidasi:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        self.__hp = hp_awal
    
    def get_hp(self):
        return self.__hp
    
    def set_hp(self, nilai_baru):
        self.__hp = nilai_baru  # BAHAYA! Tanpa validasi
    
hero2 = HeroTanpaValidasi("Zilong", 100)
hero2.set_hp(-100)
print(f"HP Zilong (tanpa validasi): {hero2.get_hp()}")  # Output: -100 (RUSAK!)
"""
