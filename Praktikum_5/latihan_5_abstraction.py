"""
LATIHAN 5: Abstraction & Interface (Membuat Kontrak/Standar)
Tujuan: Memastikan semua karakter (baik Hero maupun Monster) wajib memiliki 
        method serang dan info menggunakan modul abc
"""

from abc import ABC, abstractmethod

# 1. Interface / Abstract Class
# Ini adalah KONTRAK. Semua turunan wajib punya method di bawah ini.
class GameUnit(ABC):
    
    @abstractmethod
    def serang(self, target):
        pass
    
    @abstractmethod
    def info(self):
        pass


# 2. Implementasi pada Class Konkret
class Hero(GameUnit):
    def __init__(self, nama):
        self.nama = nama
    
    # Kita WAJIB membuat method serang, kalau tidak akan Error
    def serang(self, target):
        print(f"Hero {self.nama} menebas {target}!")
    
    def info(self):
        print(f"Saya adalah Hero: {self.nama}")


class Monster(GameUnit):
    def __init__(self, jenis):
        self.jenis = jenis
    
    # Implementasi serang versi Monster
    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target}!")
    
    def info(self):
        print(f"Saya adalah Monster: {self.jenis}")


# -- Uji Coba --
print("=== MEMBUAT HERO DAN MONSTER ===")
h = Hero("Alucard")
m = Monster("Serigala")

print("\n--- Info Unit ---")
h.info()
m.info()

print("\n--- Aksi Serang ---")
h.serang("Monster")
m.serang("Hero")

print("\n=== TUGAS ANALISIS 5 ===")
print("\n1. Mencoba membuat objek dari Abstract Class:")
try:
    unit = GameUnit()  # ERROR! Abstract class tidak bisa jadi objek.
    print("Berhasil membuat GameUnit (SEHARUSNYA INI TIDAK MUNCUL!)")
except TypeError as e:
    print(f"ERROR: {e}")
    print("^ Abstract class GameUnit tidak bisa diinstansiasi!")

print("\n2. Mencoba membuat Hero tanpa method serang:")
print("   (Uncomment kode di bawah untuk melihat error)")

"""
# Jika kita hapus method serang dari Hero:
class HeroCacat(GameUnit):
    def __init__(self, nama):
        self.nama = nama
    
    def info(self):
        print(f"Saya adalah Hero: {self.nama}")
    
    # Method serang TIDAK ada! (Melanggar kontrak)

# Mencoba membuat objek
try:
    h2 = HeroCacat("Broken Hero")
except TypeError as e:
    print(f"ERROR: {e}")
    print("^ Karena tidak mengimplementasikan method 'serang' yang wajib!")
"""

print("\nKesimpulan:")
print("- GameUnit adalah KONTRAK yang memaksa semua turunannya punya method serang() dan info()")
print("- GameUnit sendiri tidak bisa dibuat objek karena dia hanya blueprint/template")
print("- Jika class turunan lupa buat method yang dijanjikan, program akan error saat instansiasi")
