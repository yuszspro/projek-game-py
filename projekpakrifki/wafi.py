# Aplikasi Kasir Sederhana

def tampilkan_barang():
    print("=== Menu ===")
    print("1. Celana - Rp 50.000")
    print("2. Kaos - Rp 80.000")
    print("3. Topi - Rp 25.000")
    print("4. Selesai")
31
def hitung_total(pesanan):
    total = 0
    harga_barang = {
        "Celana": 50000,
        "Kaos": 80000,
        "Topi": 25000,
    }
    
    for item, jumlah in pesanan.items():
        total += harga_barang[item] * jumlah
    
    return total

def main():
    print("Selamat datang di yuszstore")
    nama_pembeli = input("Masukkan nama pembeli: ")
    
    pesanan = {}
    
    while True:
        tampilkan_barang()
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == '1':
            barang = "Celana"
        elif pilihan == '2':
            barang = "Kaos"
        elif pilihan == '3':
            barang = "Topi"
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            continue
        
        jumlah = int(input(f"Masukkan jumlah {barang} yang ingin dibeli: "))
        if barang in pesanan:
            pesanan[barang] += jumlah
        else:
            pesanan[barang] = jumlah
        
        print(f"Pesanan saat ini: {pesanan}")
    
    total_harga = hitung_total(pesanan)
    print(f"\nNama Pembeli: {nama_pembeli}")
    print(f"Pesanan: {pesanan}")
    print(f"Total Harga: Rp {total_harga}")
    
    uang_dibayar = int(input("Masukkan uang yang dibayar: "))
    
    if uang_dibayar < total_harga:
        print("Uang yang dibayar tidak cukup.")
    else:
        kembalian = uang_dibayar - total_harga
        print(f"Pembayaran: Rp {uang_dibayar}")
        print(f"Kembalian: Rp {kembalian}")

if __name__ == "__main__":
    main()