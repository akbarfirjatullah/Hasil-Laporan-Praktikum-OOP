# LATIHAN 2: Interaksi Antar Objek (Method)
# Tujuan: Membuat objek saling berinteraksi (saling serang)

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


hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)

hero1.info()
hero2.info()

print("\n--- Pertarungan Dimulai ---")
hero1.serang(hero2)
hero2.serang(hero1)  

print("\n--- Status Setelah Pertarungan ---")
hero1.info()
hero2.info()

"""
============================================================================
TUGAS ANALISIS 2 - Interaksi Antar Objek
============================================================================

PERTANYAAN:
Perhatikan parameter 'lawan' pada method serang. Parameter tersebut 
menerima sebuah objek utuh, bukan hanya string nama. Mengapa ini penting?

JAWABAN:
Parameter 'lawan' menerima OBJEK UTUH (bukan hanya string nama) karena:

1. AKSES KE ATRIBUT DAN METHOD
   - Kita perlu mengakses HP lawan untuk menguranginya
   - Kita perlu memanggil method diserang() milik lawan
   - Jika hanya string nama, kita tidak bisa mengubah data lawan

2. INTERAKSI ANTAR OBJEK
   Contoh dalam method serang():
   
   def serang(self, lawan):
       print(f"{self.name} menyerang {lawan.name}!")
       lawan.diserang(self.attack_power)  # Panggil method objek lawan
   
   - self = objek yang menyerang
   - lawan = objek yang diserang (HARUS objek lengkap)
   - lawan.diserang() = memanggil method milik objek lawan
   - lawan.name = mengakses atribut nama lawan

3. PERBANDINGAN:
   
   ❌ SALAH (hanya string):
   def serang(self, nama_lawan):
       print(f"{self.name} menyerang {nama_lawan}!")
       # STUCK! Tidak bisa kurangi HP karena hanya punya string nama
   
   ✓ BENAR (objek utuh):
   def serang(self, lawan):
       print(f"{self.name} menyerang {lawan.name}!")
       lawan.diserang(self.attack_power)  # Bisa ubah HP lawan!

KESIMPULAN:
Dengan melempar objek utuh sebagai parameter, kita bisa:
- Membaca atribut objek tersebut (lawan.name, lawan.hp)
- Memanggil method objek tersebut (lawan.diserang())
- Memodifikasi state/kondisi objek tersebut (mengubah HP)

Ini adalah konsep fundamental OOP: OBJEK SALING BERINTERAKSI.
"""
