# LATIHAN 6: Polymorphism (Fleksibilitas Interaksi)
# Tujuan: Menjalankan perintah yang sama (serang) ke berbagai jenis objek berbeda, dan hasilnya menyesuaikan masing-masing objek
        
class Hero:
    def __init__(self, nama):
        self.nama = nama
    
    def serang(self):
        print("Hero menyerang dengan tangan kosong.")


class Mage(Hero):
    def serang(self):
        print(f"{self.nama} (Mage) menembakkan Bola Api! Boom!")


class Archer(Hero):
    def serang(self):
        print(f"{self.nama} (Archer) memanah dari jauh! Jleb!")


class Fighter(Hero):
    def serang(self):
        print(f"{self.nama} (Fighter) memukul dengan pedang! Slash!")


pasukan = [
    Mage("Eudora"),
    Archer("Miya"),
    Fighter("Zilong"),
    Mage("Gord")
]

print("=== PERANG DIMULAI ===")
for pahlawan in pasukan:
    pahlawan.serang()

print("\n=== TUGAS ANALISIS 6 ===")
print("\n1. Menambahkan class Healer baru:")

class Healer(Hero):
    def serang(self):
        print(f"{self.nama} (Healer) tidak menyerang, tapi menyembuhkan teman!")

pasukan_baru = [
    Mage("Eudora"),
    Archer("Miya"),
    Fighter("Zilong"),
    Healer("Estes"),  
    Mage("Gord")
]

print("\n--- Perang dengan Healer ---")
for pahlawan in pasukan_baru:
    pahlawan.serang()  

print("\nKesimpulan:")
print("✓ Polymorphism memungkinkan kita menambah hero baru tanpa ubah kode loop")
print("✓ Ini sangat berguna saat update game dengan karakter baru di masa depan")

print("\n2. Konsistensi Penamaan:")
print("   Jika method Archer diubah dari 'serang()' ke 'tembak_panah()'...")
print("   Program akan ERROR karena loop memanggil .serang() yang tidak ada!")
print("   Karena itu, semua Child Class HARUS punya method dengan NAMA SAMA.")

# Demonstrasi error (di-comment)
"""
class ArcherBroken(Hero):
    def tembak_panah(self):  # Nama method BEDA!
        print(f"{self.nama} (Archer) memanah dari jauh!")

pasukan_error = [ArcherBroken("Miya")]
for pahlawan in pasukan_error:
    pahlawan.serang()  # ERROR! ArcherBroken tidak punya method serang()
"""

print("\n=== BONUS: Polymorphism dengan Parameter ===")

class Tank(Hero):
    def serang(self):
        print(f"{self.nama} (Tank) menabrak musuh dengan tameng! BANG!")

def mulai_perang(daftar_hero):
    """Fungsi ini menerima SEMUA jenis Hero, tanpa peduli tipenya"""
    print("\n⚔️  PERTEMPURAN DIMULAI")
    for hero in daftar_hero:
        hero.serang()  

tim_1 = [Mage("Kagura"), Tank("Tigreal")]
tim_2 = [Archer("Layla"), Fighter("Chou"), Healer("Rafaela")]

mulai_perang(tim_1)
mulai_perang(tim_2)

"""
============================================================================
TUGAS ANALISIS 6 - Polymorphism
============================================================================

PERTANYAAN 1:
Tanpa mengubah satu huruf pun pada kode Looping (for pahlawan in pasukan:),
buatlah satu class baru bernama Healer(Hero). Isi method serang milik Healer
dengan: print(f"{self.nama} tidak menyerang, tapi menyembuhkan teman!").
Masukkan objek Healer ke dalam list pasukan.
- Apakah program berjalan lancar?
- Apa keuntungan Polimorfisme bagi programmer ketika harus mengupdate game
  dengan karakter baru di masa depan?

JAWABAN:

APAKAH PROGRAM BERJALAN LANCAR?
YA! Program berjalan sempurna tanpa error.

BUKTI KODE:

# Class baru (tidak mengubah class lain)
class Healer(Hero):
    def serang(self):
        print(f"{self.nama} (Healer) tidak menyerang, tapi menyembuhkan teman!")

# Tambah ke pasukan
pasukan = [
    Mage("Eudora"),
    Archer("Miya"),
    Fighter("Zilong"),
    Healer("Estes"),  # ← HERO BARU!
    Mage("Gord")
]

# Loop TIDAK DIUBAH SAMA SEKALI
for pahlawan in pasukan:
    pahlawan.serang()  # Otomatis panggil serang() versi Healer!

OUTPUT:
Eudora (Mage) menembakkan Bola Api! Boom!
Miya (Archer) memanah dari jauh! Jleb!
Zilong (Fighter) memukul dengan pedang! Slash!
Estes (Healer) tidak menyerang, tapi menyembuhkan teman!  ← BARU!
Gord (Mage) menembakkan Bola Api! Boom!

KEUNTUNGAN POLYMORPHISM UNTUK UPDATE GAME:

1. EXTENSIBILITY (Mudah Diperluas)
   
   ✓ DENGAN POLYMORPHISM:
   - Buat class Healer baru → Selesai!
   - Tidak perlu ubah fungsi mulai_pertempuran()
   - Tidak perlu ubah loop yang sudah ada
   - Tidak perlu ubah class lain (Mage, Archer, Fighter)
   
   TANPA POLYMORPHISM:
   - Buat class Healer baru
   - Ubah fungsi mulai_pertempuran() tambahkan case Healer
   - Ubah semua kondisional if-elif di berbagai tempat
   - Ubah dokumentasi
   - Testing ulang semua kode
   
   Polymorphism = 1 langkah vs 5+ langkah!

2. OPEN/CLOSED PRINCIPLE
   
   "Software should be OPEN for extension, but CLOSED for modification"
   
   Artinya:
   - OPEN: Bisa tambah fitur baru (Healer, Tank, Assassin)
   - CLOSED: Tidak perlu ubah kode lama (loop tetap sama)
   
   Contoh update game 1 tahun kemudian:
   - Tahun 2026: Ada 5 hero (Mage, Archer, Fighter, Healer, Tank)
   - Tahun 2027: Tambah 10 hero baru (Assassin, Support, Jungler, dll)
   - Kode loop for pahlawan in pasukan: TETAP SAMA!

3. TEAM WORK & SCALABILITY
   
   Scenario: Game dikembangkan 10 programmer
   
   - Programmer A: Buat Mage
   - Programmer B: Buat Archer
   - Programmer C: Buat Fighter
   - ...
   - Programmer J: Buat Healer (6 bulan kemudian)
   
   Tanpa Polymorphism:
   - Programmer J harus baca kode semua programmer lain
   - Programmer J harus ubah fungsi milik programmer lain
   - Risk: Merusak kode yang sudah stabil
   - Conflict: Git merge hell!
   
   Dengan Polymorphism:
   - Programmer J cuma buat class Healer(Hero)
   - Tidak perlu sentuh kode programmer lain
   - Zero conflict!
   - Testing independent

4. FUTURE-PROOF CODE
   
   def mulai_pertempuran(daftar_hero):
       for hero in daftar_hero:
           hero.serang()  # Kode ini akan tetap jalan 5 tahun ke depan!
   
   Tidak peduli berapa banyak hero baru ditambahkan (50? 100?),
   fungsi ini TIDAK PERLU DIUBAH.
   
   Benefit:
   - Less bugs (kode lama = kode teruji)
   - Less maintenance cost
   - Faster development (fokus ke fitur baru, bukan perbaiki yang lama)

5. REAL-WORLD EXAMPLE: MOBILE LEGENDS
   
   Mobile Legends punya 120+ hero (2024).
   
   Tanpa Polymorphism:
   
   if hero == "Layla":
       attack_with_gun()
   elif hero == "Eudora":
       attack_with_magic()
   elif hero == "Balmond":
       attack_with_axe()
   ... (120+ elif statements!) ← NIGHTMARE!
   
   Dengan Polymorphism:
   
   for hero in all_heroes:
       hero.attack()  # ← Simple & elegant!
   
   Setiap hero baru tinggal tambah class, done!

6. PLUGIN ARCHITECTURE
   
   Polymorphism memungkinkan MODDING (user-created content):
   
   # Mod creator (bukan developer game) bisa buat hero baru
   class MyCustomHero(Hero):
       def serang(self):
           print("Custom attack animation!")
   
   # Game engine tetap bisa pakai
   game.add_hero(MyCustomHero("ModHero"))
   
   Game populer (Skyrim, Minecraft) menggunakan prinsip ini!

ANALOGI DUNIA NYATA:

Polymorphism = Colokan Listrik Universal
- Semua alat elektronik (TV, laptop, kulkas, dll) punya colokan yang sama
- Tidak perlu ubah stop kontak setiap kali beli alat baru
- Beli kulkas baru → Langsung colok → Langsung jalan!

Tanpa Polymorphism = Colokan Custom untuk Setiap Alat
- Kulkas punya stop kontak khusus kulkas
- TV punya stop kontak khusus TV
- Beli alat baru → Harus pasang stop kontak baru di dinding!

KESIMPULAN:
Polymorphism adalah INVESTASI:
✓ Effort awal sedikit lebih besar (buat parent class, abstraction)
✓ Tapi PAYOFF jangka panjang LUAR BIASA:
  - Update game 10x lebih cepat
  - Bug 10x lebih sedikit
  - Team work 10x lebih smooth
  - Maintenance cost 10x lebih murah

"Write code today that will thank you tomorrow."

============================================================================

PERTANYAAN 2:
Ubah nama method serang pada class Archer menjadi tembak_panah. 
Jalankan program. Apa yang terjadi? Mengapa dalam konsep Polimorfisme, 
nama method antara Parent Class dan berbagai Child Class harus persis sama?

JAWABAN:

APA YANG TERJADI:
AttributeError: 'Archer' object has no attribute 'serang'

PENYEBABNYA:

KODE BERMASALAH:

class Archer(Hero):
    def tembak_panah(self):  # ← Nama method BEDA!
        print(f"{self.nama} (Archer) memanah dari jauh!")

pasukan = [Mage("Eudora"), Archer("Miya"), Fighter("Zilong")]

for pahlawan in pasukan:
    pahlawan.serang()  # ← Loop mencari method 'serang'

Error di objek Miya (Archer):
- Loop panggil: miya.serang()
- Archer punya: miya.tembak_panah()
- Python: "Method 'serang' tidak ditemukan!" → ERROR!

MENGAPA NAMA METHOD HARUS SAMA:

1. KONTRAK POLYMORPHISM = INTERFACE YANG KONSISTEN
   
   Polymorphism berfungsi karena:
   "Semua Child bisa dipanggil dengan cara yang sama"
   
   Kita tidak cek tipe objek:
   if isinstance(hero, Mage): hero.attack_magic()
   elif isinstance(hero, Archer): hero.tembak_panah()
   
   Kita hanya panggil method universal:
   ✓ hero.serang()  # Semua hero WAJIB punya ini!

2. DUCK TYPING PHILOSOPHY
   
   Python: "If it walks like a duck and quacks like a duck, it's a duck"
   
   Artinya:
   - Python tidak peduli class-nya apa (Mage? Archer? Fighter?)
   - Python hanya peduli: "Punya method serang()?"
   
   Jika nama method beda → duck test gagal → error!

3. BAYANGKAN TANPA KONSISTENSI NAMA:
   
   class Mage(Hero):
       def cast_spell(self): ...
   
   class Archer(Hero):
       def shoot_arrow(self): ...
   
   class Fighter(Hero):
       def swing_sword(self): ...
   
   Loop jadi NIGHTMARE:
   for hero in pasukan:
       if isinstance(hero, Mage):
           hero.cast_spell()
       elif isinstance(hero, Archer):
           hero.shoot_arrow()
       elif isinstance(hero, Fighter):
           hero.swing_sword()
       # Setiap hero baru = tambah elif baru! ← SANGAT BURUK!
   
   Ini BUKAN polymorphism! Ini adalah PROCEDURAL dengan extra steps.

4. INTERFACE CONTRACT
   
   Parent Class = Kontrak
   Child Class = Implementor yang wajib ikuti kontrak
   
   class Hero:
       def serang(self):  # ← KONTRAK: "Semua hero wajib punya method ini"
           pass
   
   Jika Child ubah nama → Melanggar kontrak → System rusak

5. FUNCTION SIGNATURE MATCHING
   
   def battle_system(unit):
       unit.serang("enemy")  # Expect parameter ini
   
   Semua Child wajib punya:
   - Nama method: serang
   - Parameter: sama (self)
   - Return type: sama (atau compatible)
   
   Jika beda → function call gagal!

6. TOOL SUPPORT & IDE
   
   IDE (VS Code, PyCharm) bisa auto-complete:
   
   hero.se|  ← Ketik "se", IDE suggest "serang()"
   
   Karena IDE tahu: "Semua Hero punya method serang()"
   
   Jika nama beda-beda → IDE tidak bisa bantu → productivity turun!

SOLUSI: OVERRIDE, BUKAN RENAME

✓ BENAR:
class Archer(Hero):
    def serang(self):  # ← NAMA SAMA, implementasi beda
        print(f"{self.nama} memanah!")

SALAH:
class Archer(Hero):
    def tembak_panah(self):  # ← NAMA BEDA!
        print(f"{self.nama} memanah!")

ANALOGI DUNIA NYATA:

Remote Control Universal:
- Semua TV punya tombol "Power", "Volume+", "Channel+"
- Nama tombol SAMA, tapi cara kerja di balik layar beda
- TV Samsung: Power → infrared signal
- TV LG: Power → bluetooth signal
- Remote: Tidak peduli! Cukup tekan "Power"

Jika setiap TV punya nama tombol beda:
- TV Samsung: Tombol "Nyalakan"
- TV LG: Tombol "Start"
- TV Sony: Tombol "On"
→ Remote universal TIDAK MUNGKIN dibuat!

KESIMPULAN:
Nama method yang konsisten adalah FONDASI polymorphism:
✓ Memungkinkan generic programming (one loop for all types)
✓ Memudahkan maintenance (standar yang jelas)
✓ Meningkatkan readability (programmer tahu method apa yang tersedia)
✓ Mendukung tool integration (IDE, linter, type checker)

Rule of thumb:
"Method yang melakukan hal yang sama HARUS punya nama yang sama,
tidak peduli di class mana method tersebut berada."

Override = Change implementation, NOT the name!
"""
