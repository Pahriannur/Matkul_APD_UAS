from database import kursor, daftar_status
from utils import tampilkan_tabel


def cari_nama():
    kata = input("Masukkan nama pelanggan: ")
    kursor.execute("SELECT * FROM pesanan WHERE nama LIKE ?", ("%" + kata + "%",))
    hasil = kursor.fetchall()
    tampilkan_tabel("HASIL PENCARIAN", hasil)


def filter_status():
    print("1. Menunggu  2. Proses  3. Selesai")
    pilih = input("Pilih status (1-3): ")
    if pilih != "1" and pilih != "2" and pilih != "3":
        print("Pilihan tidak valid!")
        return

    status_cari = daftar_status[int(pilih) - 1]
    kursor.execute("SELECT * FROM pesanan WHERE status = ?", (status_cari,))
    hasil = kursor.fetchall()
    tampilkan_tabel("PESANAN STATUS " + status_cari.upper(), hasil)


def urutkan_deadline():
    kursor.execute("SELECT * FROM pesanan ORDER BY deadline ASC")
    hasil = kursor.fetchall()
    tampilkan_tabel("PESANAN BERDASARKAN DEADLINE TERDEKAT", hasil)


def total_pendapatan():
    total = 0
    total_selesai = 0
    kursor.execute("SELECT harga, status FROM pesanan")
    for baris in kursor.fetchall():
        total = total + baris[0]
        if baris[1] == "Selesai":
            total_selesai = total_selesai + baris[0]
    print("Total semua pesanan   : Rp", total)
    print("Pendapatan (selesai)  : Rp", total_selesai)