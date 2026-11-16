from database import buat_tabel, isi_data_awal, tutup_koneksi
from utils import bersihkan_layar, tunggu
from crud import tambah_pesanan, lihat_pesanan, edit_pesanan, hapus_pesanan
from fitur import cari_nama, filter_status, urutkan_deadline, total_pendapatan


def tampilkan_menu():
    print("=== SISTEM PENCATATAN JOKI TUGAS ===")
    print("1. Tambah Pesanan")
    print("2. Lihat Pesanan")
    print("3. Edit Pesanan")
    print("4. Hapus Pesanan")
    print("5. Cari berdasarkan nama pelanggan")
    print("6. Filter berdasarkan status")
    print("7. Urutkan berdasarkan deadline")
    print("8. Total pendapatan")
    print("9. Keluar")


def main():
    buat_tabel()
    isi_data_awal()
    while True:
        bersihkan_layar()
        tampilkan_menu()
        pilih = input("Pilih menu (1-9): ")

        if pilih == "1":
            tambah_pesanan()
        elif pilih == "2":
            lihat_pesanan()
        elif pilih == "3":
            edit_pesanan()
        elif pilih == "4":
            hapus_pesanan()
        elif pilih == "5":
            cari_nama()
        elif pilih == "6":
            filter_status()
        elif pilih == "7":
            urutkan_deadline()
        elif pilih == "8":
            total_pendapatan()
        elif pilih == "9":
            print("Terima kasih, program selesai.")
            tutup_koneksi()
            break
        else:
            print("Pilihan tidak valid!")
        tunggu()


main()