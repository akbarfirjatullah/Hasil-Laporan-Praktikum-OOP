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

"""
============================================================================
TUGAS ANALISIS 3 - Pewarisan (Inheritance)
============================================================================

PERTANYAAN:
Pada class Mage, coba hapus baris super().__init__(name, hp, attack_power).
Kemudian jalankan programnya.
- Error apa yang muncul saat kamu mencoba melihat info Eudora (eudora.info())?
- Mengapa error tersebut mengatakan 'Mage object has no attribute name'?
- Jelaskan peran fungsi super() dalam menghubungkan data dari class Anak 
  ke class Induk!

JAWABAN:

ERROR YANG MUNCUL:
AttributeError: 'Mage' object has no attribute 'name'

PENYEBABNYA:
Tanpa super().__init__(), atribut name, hp, dan attack_power TIDAK PERNAH 
DIBUAT untuk objek Mage.

PENJELASAN DETAIL:

1. BAGAIMANA SUPER() BEKERJA:
   
   class Mage(Hero):
       def __init__(self, name, hp, attack_power, mana):
           super().__init__(name, hp, attack_power)  # Panggil constructor Parent
           self.mana = mana  # Tambah atribut khusus Mage
   
   super().__init__() memanggil constructor class Hero, yang akan:
   - Membuat self.name = name
   - Membuat self.hp = hp
   - Membuat self.attack_power = attack_power

2. TANPA SUPER():
   
   class Mage(Hero):
       def __init__(self, name, hp, attack_power, mana):
           # super().__init__(name, hp, attack_power)  # DIHAPUS!
           self.mana = mana  # Hanya mana yang dibuat
   
   Yang terjadi:
   - self.mana BERHASIL dibuat ✓
   - self.name TIDAK dibuat ✗
   - self.hp TIDAK dibuat ✗
   - self.attack_power TIDAK dibuat ✗
   
   Saat eudora.info() dipanggil, dia coba akses self.name → ERROR!

3. PERAN super():
   
   super() = Jembatan antara Child Class dan Parent Class
   
   ┌─────────────┐
   │ Parent:Hero │  ← Punya atribut: name, hp, attack_power
   └──────┬──────┘
          │
     super()  ← Jembatan ini memanggil __init__ Parent
          │
   ┌──────▼──────┐
   │ Child: Mage │  ← Mewarisi atribut Parent + tambah atribut sendiri (mana)
   └─────────────┘

ANALOGI DUNIA NYATA:
Kamu mewarisi rumah dari orang tua (Parent).
- super() = Proses legal surat waris
- Tanpa super() = Kamu klaim punya rumah tapi tidak ada surat → Ditolak!

KESIMPULAN:
super().__init__() WAJIB dipanggil di constructor Child Class agar:
1. Atribut Parent bisa diinisialisasi dengan benar
2. Child Class bisa menggunakan semua fitur Parent
3. Inheritance berfungsi dengan sempurna

BEST PRACTICE:
Panggil super().__init__() sebagai BARIS PERTAMA di constructor Child Class.
"""
