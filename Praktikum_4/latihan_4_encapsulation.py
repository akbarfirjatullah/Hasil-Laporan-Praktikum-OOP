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

"""
============================================================================
TUGAS ANALISIS 4 - Enkapsulasi
============================================================================

PERTANYAAN 1:
Coba tambahkan baris: print(f"Mencoba akses paksa: {hero1._Hero__hp}")
Apakah nilai HP muncul atau Error? Jika muncul, diskusikan mengapa Python 
masih mengizinkan akses ini (konsep Name Mangling) dan mengapa kita tetap 
tidak boleh melakukannya.

JAWABAN:

HASIL:
Nilai HP MUNCUL (tidak error)! Contoh output: 0 atau angka lainnya.

PENJELASAN - NAME MANGLING:

1. BAGAIMANA PYTHON MENYIMPAN PRIVATE ATTRIBUTE:
   
   class Hero:
       def __init__(self, nama, hp_awal):
           self.__hp = hp_awal  # Terlihat private
   
   Secara internal, Python mengubah nama variabel:
   __hp → _Hero__hp (menambahkan _NamaClass di depan)
   
   Ini disebut NAME MANGLING (pengacakan nama).

2. CARA MENGAKSES:
   
   hero1 = Hero("Layla", 100)
   
   ✗ print(hero1.__hp)         # ERROR! AttributeError
   ✓ print(hero1._Hero__hp)    # BERHASIL! Tapi TIDAK DISARANKAN
   ✓ print(hero1.get_hp())     # CARA YANG BENAR

3. MENGAPA PYTHON MENGIZINKAN _Hero__hp?
   
   Python mengikuti filosofi "We're all consenting adults here":
   - Python PERCAYA programmer tahu apa yang mereka lakukan
   - Tanda __ adalah KONVENSI (kesepakatan), bukan KUNCI MUTLAK
   - Jika programmer BENAR-BENAR butuh akses darurat (debugging), 
     Python memberi jalan lewat name mangling

4. MENGAPA TETAP TIDAK BOLEH?
   
   JANGAN pakai hero1._Hero__hp karena:
   
   a) MELANGGAR KONTRAK OOP
      - Encapsulation = "Data private, akses lewat method"
      - Akses langsung = melanggar kontrak
   
   b) MERUSAK VALIDASI
      hero1._Hero__hp = -9999  # Bypass setter validation!
      - Setter punya logika agar HP tidak negatif
      - Akses langsung = mengabaikan perlindungan
   
   c) CODE MAINTENANCE NIGHTMARE
      - Jika nama class Hero diubah jadi Character, semua 
        _Hero__hp harus diganti jadi _Character__hp
      - Jika nama atribut __hp diubah jadi __health, semua 
        _Hero__hp harus diganti jadi _Hero__health
   
   d) TEAM WORK ISSUE
      - Programmer lain tidak akan paham kenapa kamu akses langsung
      - Merusak standar kode yang sudah disepakati

KESIMPULAN:
- Name Mangling = Pintu darurat yang dibiarkan terbuka oleh Python
- JANGAN pakai kecuali situasi SANGAT KHUSUS (debugging internal)
- SELALU gunakan Getter/Setter untuk akses data private
- "Just because you CAN, doesn't mean you SHOULD"

============================================================================

PERTANYAAN 2:
Hapus logika if dan elif di method set_hp, sehingga isinya hanya 
self.__hp = nilai_baru. Kemudian lakukan hero1.set_hp(-100). 
Apa yang terjadi pada data HP Hero? Jelaskan mengapa keberadaan method 
Setter sangat penting untuk menjaga integritas data dalam game!

JAWABAN:

HASIL:
HP menjadi -100 (nilai negatif yang tidak masuk akal dalam game!)

PERBANDINGAN:

TANPA VALIDASI:
def set_hp(self, nilai_baru):
    self.__hp = nilai_baru  # Langsung set tanpa cek

hero1.set_hp(-100)
print(hero1.get_hp())  # Output: -100 ← DATA RUSAK!

✓ DENGAN VALIDASI:
def set_hp(self, nilai_baru):
    if nilai_baru < 0:
        self.__hp = 0  # Cegah nilai negatif
    elif nilai_baru > 1000:
        print("Cheat terdeteksi!")
        self.__hp = 1000
    else:
        self.__hp = nilai_baru

hero1.set_hp(-100)
print(hero1.get_hp())  # Output: 0 ← DATA AMAN!

MENGAPA SETTER SANGAT PENTING:

1. VALIDASI DATA (Data Integrity)
   - Mencegah nilai tidak logis (HP negatif, HP 999999)
   - Memastikan data selalu dalam rentang yang valid
   - Melindungi dari input yang salah atau sengaja dirusak

2. BUSINESS LOGIC ENFORCEMENT
   Contoh rules dalam game:
   - HP tidak boleh < 0 (hero mati)
   - HP tidak boleh > max_hp (tidak bisa overheal)
   - HP harus kelipatan 10 (game design)
   
   Semua rule ini bisa diterapkan di Setter.

3. DEBUGGING & LOGGING
   def set_hp(self, nilai_baru):
       print(f"[LOG] HP diubah dari {self.__hp} ke {nilai_baru}")
       if nilai_baru < 0:
           print("[WARNING] Deteksi cheat! HP negatif dicegah.")
           self.__hp = 0
       else:
           self.__hp = nilai_baru
   
   Kita bisa track semua perubahan HP!

4. BACKWARD COMPATIBILITY
   Jika game di-update dan rule HP berubah:
   - Cukup ubah logic di Setter
   - Semua kode yang pakai set_hp() otomatis ikut rule baru
   - Tidak perlu ubah ratusan baris kode

ANALOGI DUNIA NYATA:
Setter = Security Guard di bank
- Cek identitas sebelum masuk (validasi)
- Tolak orang mencurigakan (nilai invalid)
- Catat siapa saja yang masuk (logging)
- Tanpa security = siapa saja bisa masuk dan rusak data!

KESIMPULAN:
Setter bukan sekadar "cara mengubah variabel", tapi GERBANG PENJAGA
yang memastikan:
✓ Data selalu valid
✓ Business rules diterapkan
✓ System tetap stabil dan aman dari manipulasi

Dalam game profesional, SEMUA atribut kritis (HP, mana, gold, level, dll) 
WAJIB pakai Setter dengan validasi ketat.
"""
