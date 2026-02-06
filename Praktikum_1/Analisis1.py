print("=" * 70)
print("TUGAS ANALISIS 1 - Membuat Class Hero")
print("=" * 70)

print("""
PERTANYAAN:
Apa yang terjadi jika kamu mengubah hero1.hp menjadi 500 setelah baris 
hero1 = Hero...? Coba lakukan print(hero1.hp).

JAWABAN:
Ketika kita mengubah hero1.hp = 500 setelah objek hero1 dibuat, nilai HP 
akan berubah dari 100 menjadi 500.

CONTOH:
hero1 = Hero("Layla", 100, 15)
print(hero1.hp)  # Output: 100
hero1.hp = 500
print(hero1.hp)  # Output: 500

PENJELASAN:
- Atribut 'hp' bersifat PUBLIC (bisa diakses dan diubah dari luar class)
- Ini adalah salah satu kelemahan jika tidak menggunakan ENCAPSULATION
- Siapa saja bisa mengubah HP secara langsung, bahkan membuat HP negatif 
  atau nilai tidak wajar seperti 99999 (cheating)
- Untuk mencegah ini, kita perlu menggunakan Private Attribute dan 
  Getter/Setter (akan dipelajari di Latihan 4)

KESIMPULAN:
Tanpa enkapsulasi, data objek rentan terhadap manipulasi yang tidak 
terkontrol. Ini berbahaya untuk integritas data dalam aplikasi nyata.
""")
