"""
TUGAS PROYEK INTEGRASI: Sistem Manajemen Inventaris "TechMaster"
Tingkat Kesulitan: Advanced (Mencakup 4 Pilar OOP)

Skenario:
Toko elektronik "TechMaster" membutuhkan sistem backend untuk mengelola stok
barang mereka (Laptop dan Smartphone). Data stok dan harga harus dilindungi,
dan setiap jenis barang memiliki cara perhitungan pajak yang berbeda.
"""

from abc import ABC, abstractmethod


# ============================================================================
# PILAR 1: ABSTRACTION (Kerangka Dasar)
# ============================================================================
class BarangElektronik(ABC):
    """
    Abstract Class sebagai blueprint untuk semua barang elektronik.
    Tidak bisa diinstansiasi langsung.
    """
    
    def __init__(self, nama, harga_dasar, stok_awal):
        self.nama = nama
        self.__harga_dasar = harga_dasar 
        self.__stok = stok_awal  
    
    # PILAR 2: ENCAPSULATION - Getter
    def get_stok(self):
        """Getter untuk melihat stok"""
        return self.__stok
    
    def get_harga_dasar(self):
        """Getter untuk melihat harga dasar"""
        return self.__harga_dasar
    
    # PILAR 2: ENCAPSULATION - Setter dengan Validasi
    def tambah_stok(self, jumlah):
        """Menambah stok dengan validasi"""
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
            return False
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {self.__stok} unit.")
            return True
    
    def kurangi_stok(self, jumlah):
        """Mengurangi stok (untuk transaksi)"""
        if jumlah > self.__stok:
            print(f"Stok {self.nama} tidak cukup! Tersedia: {self.__stok}, diminta: {jumlah}")
            return False
        self.__stok -= jumlah
        return True
    
    @abstractmethod
    def tampilkan_detail(self):
        """Menampilkan detail barang"""
        pass
    
    @abstractmethod
    def hitung_harga_total(self, jumlah):
        """Menghitung harga total + pajak"""
        pass


# ============================================================================
# PILAR 3: INHERITANCE (Pewarisan)
# ============================================================================
class Laptop(BarangElektronik):
    """Class Laptop dengan pajak 10%"""
    
    def __init__(self, nama, harga_dasar, stok_awal, processor):
        super().__init__(nama, harga_dasar, stok_awal)
        self.processor = processor
    
    # PILAR 4: POLYMORPHISM - Override method parent
    def tampilkan_detail(self):
        """Implementasi spesifik untuk Laptop"""
        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")
        harga = self.get_harga_dasar()
        pajak = harga * 0.10
        print(f" Harga Dasar: Rp {harga:,.0f} | Pajak(10%): Rp {pajak:,.0f}")
    
    def hitung_harga_total(self, jumlah):
        """Hitung harga total dengan pajak 10%"""
        harga_dasar = self.get_harga_dasar()
        pajak = harga_dasar * 0.10
        harga_per_unit = harga_dasar + pajak
        return harga_per_unit * jumlah


class Smartphone(BarangElektronik):
    """Class Smartphone dengan pajak 5%"""
    
    def __init__(self, nama, harga_dasar, stok_awal, kamera):
        super().__init__(nama, harga_dasar, stok_awal)
        self.kamera = kamera
    
    # PILAR 4: POLYMORPHISM - Override method parent
    def tampilkan_detail(self):
        """Implementasi spesifik untuk Smartphone"""
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")
        harga = self.get_harga_dasar()
        pajak = harga * 0.05
        print(f" Harga Dasar: Rp {harga:,.0f} | Pajak(5%): Rp {pajak:,.0f}")
    
    def hitung_harga_total(self, jumlah):
        """Hitung harga total dengan pajak 5%"""
        harga_dasar = self.get_harga_dasar()
        pajak = harga_dasar * 0.05
        harga_per_unit = harga_dasar + pajak
        return harga_per_unit * jumlah


# ============================================================================
# PILAR 4: POLYMORPHISM (Fleksibilitas)
# ============================================================================
def proses_transaksi(daftar_barang):
    """
    Fungsi untuk memproses transaksi dari berbagai jenis barang.
    Menerima list berisi tuple: (objek_barang, jumlah_beli)
    
    Ini adalah contoh Polymorphism: satu fungsi bisa handle
    berbagai jenis objek (Laptop, Smartphone) tanpa perlu tahu jenisnya.
    """
    print("\n--- STRUK TRANSAKSI ---")
    total_tagihan = 0
    nomor = 1
    
    for barang, jumlah in daftar_barang:
        if not barang.kurangi_stok(jumlah):
            print(f"⚠️  Transaksi {barang.nama} dibatalkan!\n")
            continue
        
        print(f"{nomor}. ", end="")
        barang.tampilkan_detail()
        
        subtotal = barang.hitung_harga_total(jumlah)
        print(f" Beli: {jumlah} unit | Subtotal: Rp {subtotal:,.0f}\n")
        
        total_tagihan += subtotal
        nomor += 1
    
    print("-" * 40)
    print(f"TOTAL TAGIHAN: Rp {total_tagihan:,.0f}")
    print("-" * 40)


# ============================================================================
# MAIN PROGRAM - Alur Cerita
# ============================================================================
def main():
    print("=" * 50)
    print("   SISTEM MANAJEMEN INVENTARIS TECHMASTER")
    print("=" * 50)
    
    # 1. Admin membuat data produk
    print("\n--- SETUP DATA ---")
    laptop_rog = Laptop("ROG Zephyrus", 20_000_000, 0, "Ryzen 9")
    iphone = Smartphone("iPhone 13", 15_000_000, 0, "12MP")
    
    # 2. Admin mengisi stok
    laptop_rog.tambah_stok(10)
    
    # 3. Admin mencoba mengisi stok negatif (akan ditolak)
    iphone.tambah_stok(-5)
    
    # 4. Admin mengisi stok dengan benar
    iphone.tambah_stok(20)
    
    # 5. User membeli barang
    keranjang_belanja = [
        (laptop_rog, 2),  # Beli 2 Laptop
        (iphone, 1)       # Beli 1 Smartphone
    ]
    
    proses_transaksi(keranjang_belanja)
    
    # 6. Cek stok tersisa
    print("\n--- STOK TERSISA ---")
    print(f"Stok {laptop_rog.nama}: {laptop_rog.get_stok()} unit")
    print(f"Stok {iphone.nama}: {iphone.get_stok()} unit")
    
    # 7. Demonstrasi: Tidak bisa instansiasi Abstract Class
    print("\n--- UJI COBA ABSTRACTION ---")
    try:
        barang = BarangElektronik("Test", 1000, 10)
        print("Berhasil buat objek BarangElektronik (INI SEHARUSNYA ERROR!)")
    except TypeError as e:
        print(f"✓ Error (Expected): {e}")
        print("  Abstract class tidak bisa diinstansiasi!")
    
    # 8. Demonstrasi: Encapsulation (tidak bisa akses langsung)
    print("\n--- UJI COBA ENCAPSULATION ---")
    try:
        print(laptop_rog.__stok)
    except AttributeError as e:
        print(f"✓ Error (Expected): {e}")
        print("  Atribut private tidak bisa diakses langsung!")
        print(f"  Gunakan getter: {laptop_rog.get_stok()} unit")


# ============================================================================
# BONUS: Demonstrasi Polymorphism Lebih Lanjut
# ============================================================================
def demo_polymorphism():
    """Fungsi tambahan untuk mendemonstrasikan kekuatan polymorphism"""
    print("\n" + "=" * 50)
    print("   BONUS: DEMO POLYMORPHISM")
    print("=" * 50)
    
    # Berbagai jenis barang elektronik
    produk_list = [
        Laptop("MacBook Pro", 25_000_000, 5, "Apple M3"),
        Smartphone("Samsung S24", 12_000_000, 10, "200MP"),
        Laptop("ThinkPad X1", 18_000_000, 8, "Intel i9"),
        Smartphone("Xiaomi 14", 8_000_000, 15, "50MP")
    ]
    
    print("\n--- KATALOG PRODUK ---")
    for i, produk in enumerate(produk_list, 1):
        print(f"\n{i}. ", end="")
        produk.tampilkan_detail()  


# ============================================================================
# JALANKAN PROGRAM
# ============================================================================
if __name__ == "__main__":
    main()
    demo_polymorphism()
    
    print("\n" + "=" * 50)
    print("   PROGRAM SELESAI")
    print("=" * 50)
