"""
LATIHAN 6: Polymorphism (Fleksibilitas Interaksi)
Tujuan: Menjalankan perintah yang sama (serang) ke berbagai jenis objek berbeda,
        dan hasilnya menyesuaikan masing-masing objek
"""

# Parent Class
class Hero:
    def __init__(self, nama):
        self.nama = nama
    
    def serang(self):
        print("Hero menyerang dengan tangan kosong.")


# Child Class 1
class Mage(Hero):
    def serang(self):
        print(f"{self.nama} (Mage) menembakkan Bola Api! Boom!")


# Child Class 2
class Archer(Hero):
    def serang(self):
        print(f"{self.nama} (Archer) memanah dari jauh! Jleb!")


# Child Class 3
class Fighter(Hero):
    def serang(self):
        print(f"{self.nama} (Fighter) memukul dengan pedang! Slash!")


# -- Penerapan Polymorphism --
# Kita punya daftar hero campuran
pasukan = [
    Mage("Eudora"),
    Archer("Miya"),
    Fighter("Zilong"),
    Mage("Gord")
]

print("=== PERANG DIMULAI ===")
# Satu perintah loop, tapi respon berbeda-beda (Polymorphism)
for pahlawan in pasukan:
    pahlawan.serang()

print("\n=== TUGAS ANALISIS 6 ===")
print("\n1. Menambahkan class Healer baru:")

# Class baru tanpa mengubah kode loop
class Healer(Hero):
    def serang(self):
        print(f"{self.nama} (Healer) tidak menyerang, tapi menyembuhkan teman!")

# Menambahkan Healer ke pasukan
pasukan_baru = [
    Mage("Eudora"),
    Archer("Miya"),
    Fighter("Zilong"),
    Healer("Estes"),  # Hero baru!
    Mage("Gord")
]

print("\n--- Perang dengan Healer ---")
for pahlawan in pasukan_baru:
    pahlawan.serang()  # Kode loop SAMA PERSIS, tapi otomatis handle Healer!

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
    print("\n⚔️  PERTEMPURAN DIMULAI ⚔️")
    for hero in daftar_hero:
        hero.serang()  # Polymorphism: satu method, banyak bentuk hasil

# Bisa dipanggil dengan kombinasi hero apa saja
tim_1 = [Mage("Kagura"), Tank("Tigreal")]
tim_2 = [Archer("Layla"), Fighter("Chou"), Healer("Rafaela")]

mulai_perang(tim_1)
mulai_perang(tim_2)
