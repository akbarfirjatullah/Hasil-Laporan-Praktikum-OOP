# LATIHAN 5: Abstraction & Interface (Membuat Kontrak/Standar)
# Tujuan: Memastikan semua karakter (baik Hero maupun Monster) wajib memiliki method serang dan info menggunakan modul abc

from abc import ABC, abstractmethod

class GameUnit(ABC):
    
    @abstractmethod
    def serang(self, target):
        pass
    
    @abstractmethod
    def info(self):
        pass


class Hero(GameUnit):
    def __init__(self, nama):
        self.nama = nama
    
    def serang(self, target):
        print(f"Hero {self.nama} menebas {target}!")
    
    def info(self):
        print(f"Saya adalah Hero: {self.nama}")


class Monster(GameUnit):
    def __init__(self, jenis):
        self.jenis = jenis
    
    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target}!")
    
    def info(self):
        print(f"Saya adalah Monster: {self.jenis}")


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
    unit = GameUnit() 
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

"""
============================================================================
TUGAS ANALISIS 5 - Abstraction & Interface
============================================================================

PERTANYAAN 1:
Pada class Hero, hapus seluruh blok method def serang(self, target):. 
Jalankan programnya. Error apa yang muncul? Jelaskan apa arti pesan error 
"Can't instantiate abstract class Hero with abstract method..."?
Apa konsekuensinya jika kita lupa membuat method yang sudah dijanjikan 
di Interface?

JAWABAN:

ERROR YANG MUNCUL:
TypeError: Can't instantiate abstract class Hero with abstract method serang

PENJELASAN ERROR:

1. APA YANG TERJADI:
   
   from abc import ABC, abstractmethod
   
   class GameUnit(ABC):
       @abstractmethod
       def serang(self, target):
           pass
   
   class Hero(GameUnit):
       def __init__(self, nama):
           self.nama = nama
       
       # Method serang() TIDAK ADA! ← MELANGGAR KONTRAK
       
       def info(self):
           print(f"Saya adalah Hero: {self.nama}")
   
   h = Hero("Alucard")  # ← ERROR DI SINI!

2. MENGAPA ERROR:
   
   GameUnit (Parent) adalah ABSTRACT CLASS dengan ABSTRACT METHOD serang().
   
   Aturan Abstract Class:
   - Semua @abstractmethod di Parent WAJIB diimplementasi di Child
   - Jika Child tidak implementasi → Child tetap dianggap abstract
   - Abstract class TIDAK BISA dibuat objeknya
   
   Hero tidak punya method serang() → Hero masih abstract → ERROR saat dibuat objek

3. ARTI PESAN ERROR:
   
   "Can't instantiate abstract class Hero with abstract method serang"
   
   Artinya:
   - instantiate = membuat objek (instance)
   - abstract class Hero = class Hero masih berstatus abstract
   - with abstract method serang = karena method serang belum dibuat
   - Can't = Python MELARANG objek dibuat dari class abstract

4. KONSEKUENSI MELANGGAR KONTRAK:
   
   Jika lupa buat method yang dijanjikan:
   
   a) COMPILE-TIME ERROR (Python langsung tolak)
      - Program tidak bisa dijalankan sama sekali
      - Error muncul saat mencoba membuat objek
      - Ini adalah PROTEKSI dari Python
   
   b) MENCEGAH INKONSISTENSI
      Bayangkan punya fungsi:
      
      def mulai_pertempuran(unit_list):
          for unit in unit_list:
              unit.serang("musuh")  # Expect semua unit punya serang()
      
      Jika Hero tidak punya serang() → ERROR saat dipanggil!
      Abstract class mencegah ini dengan memaksa implementasi.
   
   c) TEAM WORK CHAOS
      - Programmer A: "Semua GameUnit harus punya serang()"
      - Programmer B: Lupa buat serang() di class Wizard
      - Programmer C: Pakai Wizard di battle system → CRASH!
      
      Abstract class = Memaksa programmer B ingat kontrak

5. KAPAN KONTRAK INI BERGUNA:
   
   Contoh: Game dengan 100 jenis karakter
   - Semua WAJIB punya: serang(), info(), mati()
   - Interface GameUnit memastikan tidak ada yang lupa
   - Jika ada class baru (Dragon, Goblin, dll), Python akan
     paksa mereka implementasi method wajib

ANALOGI DUNIA NYATA:
Interface = Kontrak kerja
- "Semua karyawan WAJIB punya: email, nomor HP, rekening bank"
- Jika calon karyawan tidak bisa kasih data ini → tidak bisa direkrut
- Abstract class = HR system yang otomatis tolak pendaftaran tidak lengkap

KESIMPULAN:
Abstract method adalah KONTRAK yang MEMAKSA konsistensi:
✓ Semua Child Class wajib implement method yang sama
✓ Mencegah lupa (compile-time error, bukan runtime error)
✓ Memudahkan team work dan maintenance
✓ Membuat kode lebih predictable dan safe

Melanggar kontrak = Program tidak bisa jalan sama sekali (by design).

============================================================================

PERTANYAAN 2:
Coba aktifkan baris kode unit = GameUnit(). Mengapa class GameUnit dilarang 
untuk dibuat menjadi objek? Apa gunanya ada class GameUnit jika tidak bisa 
dibuat menjadi objek nyata?

JAWABAN:

ERROR YANG MUNCUL:
TypeError: Can't instantiate abstract class GameUnit with abstract methods info, serang

MENGAPA GAMEUNIT TIDAK BISA JADI OBJEK:

1. GAMEUNIT = BLUEPRINT, BUKAN PRODUK JADI
   
   class GameUnit(ABC):  # ABC = Abstract Base Class
       @abstractmethod
       def serang(self, target):
           pass  # Tidak ada implementasi!
   
   GameUnit hanya TEMPLATE kosong:
   - Punya nama method (serang), tapi tidak ada isinya
   - Seperti blueprint arsitektur: ada desain, belum jadi bangunan
   - Tidak masuk akal membuat objek dari sesuatu yang tidak lengkap

2. FILOSOFI OOP:
   
   "GameUnit" terlalu ABSTRAK untuk jadi objek nyata:
   - Tidak ada "unit game" secara umum di dunia nyata
   - Yang ada: Hero, Monster, NPC (bentuk konkret dari GameUnit)
   - Ini seperti tidak ada "Hewan" yang berjalan di jalan,
     yang ada: Kucing, Anjing, Burung (bentuk konkret dari Hewan)

3. MEMAKSA PROGRAMMER BUAT CHILD CLASS:
   
   Python sengaja larang GameUnit jadi objek agar:
   - Programmer WAJIB buat turunannya (Hero, Monster)
   - Turunan wajib implement method (serang, info)
   - Tidak ada objek "setengah jadi" yang beredar di program

APA GUNANYA GAMEUNIT JIKA TIDAK BISA JADI OBJEK?

1. STANDARDISASI (Membuat Aturan Seragam)
   
   class GameUnit(ABC):
       @abstractmethod
       def serang(self, target):
           pass
       
       @abstractmethod
       def info(self):
           pass
   
   Artinya: "SEMUA unit game (Hero, Monster, NPC) WAJIB punya 2 method ini!"
   
   Benefit:
   - Programmer tahu apa yang harus dibuat
   - Code reviewer bisa cek: "Sudah ada serang()? Sudah ada info()?"
   - Testing jadi mudah: "Semua GameUnit pasti bisa diserang"

2. POLYMORPHISM (Bisa Diperlakukan Sama)
   
   def mulai_pertempuran(unit_list):  # Terima list GameUnit apapun
       for unit in unit_list:
           unit.serang("musuh")  # Kita yakin PASTI ada method serang()
   
   # Panggil dengan berbagai jenis unit
   pasukan = [Hero("Alucard"), Monster("Dragon"), NPC("Guard")]
   mulai_pertempuran(pasukan)  # Semua bisa serang!
   
   Tanpa GameUnit → Kita tidak yakin semua unit punya serang()

3. TYPE HINTING (Dokumentasi Kode)
   
   def tambah_ke_team(unit: GameUnit):  # Parameter wajib turunan GameUnit
       team.append(unit)
   
   IDE akan warning jika kita coba masukkan objek yang bukan GameUnit.

4. SHARED LOGIC (Kode Bersama)
   
   class GameUnit(ABC):
       def __init__(self, nama):
           self.nama = nama
           self.alive = True
       
       @abstractmethod
       def serang(self, target):
           pass
       
       def mati(self):  # Method biasa (bukan abstract)
           self.alive = False
           print(f"{self.nama} telah mati!")
   
   Benefit:
   - Semua Child (Hero, Monster) otomatis punya atribut alive
   - Semua Child bisa pakai method mati() tanpa tulis ulang
   - DRY Principle: Don't Repeat Yourself

ANALOGI DUNIA NYATA:

GameUnit = Standar ISO untuk produk elektronik
- ISO tidak bisa "dibeli" atau "dipakai" langsung
- Tapi semua produk (TV, AC, Kulkas) WAJIB ikuti standar ISO
- Benefit: Semua produk punya colokan yang sama, aman dipakai

VISUALISASI:

         ┌──────────────┐
         │  GameUnit    │  ← Abstract (tidak bisa jadi objek)
         │  (Template)  │
         └───────┬──────┘
                 │
        ┌────────┴────────┐
        │                 │
   ┌────▼────┐      ┌─────▼─────┐
   │  Hero   │      │  Monster  │  ← Concrete (bisa jadi objek)
   │ (Nyata) │      │  (Nyata)  │
   └─────────┘      └───────────┘
        │                 │
    Alucard           Dragon

KESIMPULAN:
GameUnit tidak bisa jadi objek, tapi dia SANGAT BERGUNA sebagai:
✓ KONTRAK yang memaksa konsistensi
✓ TEMPLATE yang bisa dishare ke semua Child
✓ TYPE yang bisa dipakai untuk polymorphism
✓ DOKUMENTASI yang menjelaskan "apa yang wajib ada"

"The best code is the code that doesn't let you make mistakes."
Abstract class adalah penjaga yang mencegah programmer membuat objek
yang tidak lengkap atau tidak konsisten.
"""
