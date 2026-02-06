# 📚 Modul Pembelajaran OOP Python - Kelas XI RPL 3

**Nama Siswa:** Muhammad Aulia Akbar Firjatullah 
**Kelas:** XI RPL 3  
**Mata Pelajaran:** Koding dan Kecerdasan Artificial  
**Guru:** Muhamad Arifin  
**Tanggal Pengumpulan:** 5 Februari 2026

---

## 📖 Deskripsi

Repository ini berisi hasil pengerjaan **Modul Ajar Pemrograman Berorientasi Objek (OOP) dengan Python**. Modul ini mencakup 6 latihan praktikum dan 1 proyek kelompok yang mengimplementasikan 4 pilar utama OOP: **Abstraction**, **Encapsulation**, **Inheritance**, dan **Polymorphism**.

---

## 📝 Ringkasan Latihan Praktikum

### **Latihan 1: Membuat Class Hero**
**Konsep:** Class, Object, Constructor (`__init__`), Attribute, Method

**Apa yang Dipelajari:**
- Cara membuat class sebagai blueprint
- Membuat object (instance) dari class
- Menggunakan constructor untuk inisialisasi atribut
- Membuat method untuk menampilkan informasi

**Output:**
```
Hero: Layla | HP: 100 | Power: 15
Hero: Zilong | HP: 120 | Power: 20
```

**Analisis:**
Atribut yang bersifat public dapat diubah langsung dari luar class (`hero1.hp = 500`), yang dapat menyebabkan data tidak konsisten. Ini akan diperbaiki dengan enkapsulasi di Latihan 4.

---

### **Latihan 2: Interaksi Antar Objek**
**Konsep:** Method dengan parameter object, interaksi antar object

**Apa yang Dipelajari:**
- Cara membuat method yang menerima object lain sebagai parameter
- Interaksi antar object melalui method
- Mengubah state object lain melalui method

**Output:**
```
--- Pertarungan Dimulai ---
Layla menyerang Zilong!
Zilong terkena damage 15. Sisa HP: 105
Zilong menyerang Layla!
Layla terkena damage 20. Sisa HP: 80
```

**Analisis:**
Parameter `lawan` harus berupa object utuh (bukan hanya string nama) karena kita perlu mengakses atribut dan memanggil method dari object tersebut untuk mengubah state-nya.

---

### **Latihan 3: Pewarisan (Inheritance)**
**Konsep:** Inheritance, Parent Class, Child Class, `super()`

**Apa yang Dipelajari:**
- Cara membuat child class yang mewarisi parent class
- Menggunakan `super()` untuk memanggil constructor parent
- Menambahkan atribut dan method khusus di child class
- Override method parent di child class

**Output:**
```
Eudora [Mage] | HP: 80 | Mana: 100
Eudora menyerang Balmond!
Balmond terkena damage 30. Sisa HP: 170
Eudora menggunakan Fireball ke Balmond!
Balmond terkena damage 60. Sisa HP: 110
```

**Analisis:**
`super().__init__()` WAJIB dipanggil untuk menginisialisasi atribut dari parent class. Tanpa ini, child class tidak akan memiliki atribut yang didefinisikan di parent, menyebabkan `AttributeError`.

---

### **Latihan 4: Enkapsulasi (Encapsulation)**
**Konsep:** Private attribute (`__`), Getter, Setter, Validation

**Apa yang Dipelajari:**
- Membuat atribut private dengan prefix `__`
- Membuat getter untuk membaca atribut private
- Membuat setter dengan validasi untuk mengubah atribut private
- Melindungi data dari akses dan modifikasi tidak sah

**Output:**
```
HP Layla setelah set -50: 0
Cheat terdeteksi! HP dimaksimalkan ke 1000 saja.
HP Layla setelah cheat: 1000
```

**Analisis:**
Setter dengan validasi mencegah nilai yang tidak valid (HP negatif, HP terlalu besar) dan menjaga integritas data dalam aplikasi. Name Mangling (`_Hero__hp`) bisa diakses tapi tidak boleh dilakukan karena melanggar prinsip enkapsulasi.

---

### **Latihan 5: Abstraksi & Interface**
**Konsep:** Abstract Base Class (ABC), `@abstractmethod`, Interface

**Apa yang Dipelajari:**
- Membuat abstract class dengan modul `abc`
- Mendefinisikan abstract method yang wajib diimplementasi
- Memaksa konsistensi method di semua child class
- Abstract class tidak bisa diinstansiasi

**Output:**
```
Saya adalah Hero: Alucard
Saya adalah Monster: Serigala
Hero Alucard menebas Monster!
Monster Serigala menggigit Hero!
```

**Analisis:**
Abstract class berguna sebagai template/kontrak untuk memastikan semua child class memiliki method yang sama, menjaga konsistensi dan mencegah error runtime.

---

### **Latihan 6: Polimorfisme (Polymorphism)**
**Konsep:** Method overriding, Dynamic dispatch, Generic programming

**Apa yang Dipelajari:**
- Cara membuat method dengan nama sama tapi implementasi berbeda
- Menggunakan satu loop untuk berbagai jenis object
- Extensibility: menambah class baru tanpa ubah kode existing

**Output:**
```
--- PERANG DIMULAI ---
Eudora (Mage) menembakkan Bola Api! Boom!
Miya (Archer) memanah dari jauh! Jleb!
Zilong (Fighter) memukul dengan pedang! Slash!
Estes (Healer) tidak menyerang, tapi menyembuhkan teman!
Gord (Mage) menembakkan Bola Api! Boom!
```

**Analisis:**
Polymorphism memungkinkan extensibility - menambah class baru (`Healer`) tanpa mengubah kode loop yang sudah ada. Method harus bernama sama di semua class agar polymorphism bekerja.

---

## Proyek Kelompok: TechMaster Inventory System

### **Deskripsi Proyek**
Sistem manajemen inventaris untuk toko elektronik "TechMaster" yang menjual Laptop dan Smartphone. Sistem ini mengimplementasikan keempat pilar OOP.

### **Fitur Utama**
1. **Abstraction:** Abstract class `BarangElektronik` sebagai template
2. **Encapsulation:** Private attributes dengan getter/setter dan validasi
3. **Inheritance:** Class `Laptop` dan `Smartphone` mewarisi `BarangElektronik`
4. **Polymorphism:** Perhitungan pajak berbeda (Laptop 10%, Smartphone 5%)

### **Anggota Kelompok**
- Muhammad Aulia Akbar Firjatullah
- Hafizh Adilah Athaullah

### **Cara Menjalankan**
```bash
python project_techmaster.py
```

### **Output Program**
```
--- SETUP DATA ---
Berhasil menambahkan stok ROG Zephyrus: 10 unit.
Gagal update stok iPhone 13! Stok tidak boleh negatif (-5).
Berhasil menambahkan stok iPhone 13: 20 unit.

--- STRUK TRANSAKSI ---
1. [LAPTOP] ROG Zephyrus | Proc: Ryzen 9
   Harga Dasar: Rp 20.000.000 | Pajak(10%): Rp 2.000.000
   Beli: 2 unit | Subtotal: Rp 44.000.000

2. [SMARTPHONE] iPhone 13 | Cam: 12MP
   Harga Dasar: Rp 15.000.000 | Pajak(5%): Rp 750.000
   Beli: 1 unit | Subtotal: Rp 15.750.000
----------------------------------------
TOTAL TAGIHAN: Rp 59.750.000
----------------------------------------
```
