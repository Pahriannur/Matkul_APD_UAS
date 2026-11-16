import os
from datetime import date
from prettytable import PrettyTable
from database import kursor


def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def tunggu():
    input("Tekan Enter untuk lanjut...")


def validasi_angka(teks):
    # cek huruf per huruf, True kalau semuanya angka
    if teks == "":
        return False
    for huruf in teks:
        if huruf not in "0123456789":
            return False
    return True


def input_harga():
    while True:
        harga_teks = input("Harga layanan  : ")
        if validasi_angka(harga_teks):
            return int(harga_teks)
        print("Harga harus berupa angka!")


def input_status():
    print("Status: 1. Menunggu  2. Proses  3. Selesai")
    pilih = input("Pilih status (1-3): ")
    if pilih == "2":
        return "Proses"
    elif pilih == "3":
        return "Selesai"
    else:
        return "Menunggu"


def cari_by_id(id_cari):
    # mengembalikan satu baris pesanan, atau None kalau tidak ada
    if not validasi_angka(id_cari):
        return None
    kursor.execute("SELECT * FROM pesanan WHERE id = ?", (int(id_cari),))
    return kursor.fetchone()


def jumlah_hari_bulan(tahun, bulan):
    hari_per_bulan = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if bulan == 2:
        if (tahun % 4 == 0 and tahun % 100 != 0) or tahun % 400 == 0:
            return 29
    return hari_per_bulan[bulan - 1]


def validasi_tanggal(teks):
    # format harus YYYY-MM-DD, dicek huruf per huruf
    if len(teks) != 10:
        return False
    nomor = 0
    for huruf in teks:
        if nomor == 4 or nomor == 7:
            if huruf != "-":
                return False
        else:
            if huruf not in "0123456789":
                return False
        nomor = nomor + 1

    tahun = int(teks[0:4])
    bulan = int(teks[5:7])
    hari = int(teks[8:10])
    if tahun < 2000:
        return False
    if bulan < 1 or bulan > 12:
        return False
    if hari < 1 or hari > jumlah_hari_bulan(tahun, bulan):
        return False
    return True


def input_deadline():
    while True:
        deadline = input("Deadline (YYYY-MM-DD): ")
        if validasi_tanggal(deadline):
            return deadline
        print("Format tanggal salah atau tanggal tidak ada! Contoh: 2026-11-20")


def hitung_sisa_hari(deadline, status):
    if status == "Selesai":
        return "-"
    if not validasi_tanggal(deadline):
        return "-"
    tahun = int(deadline[0:4])
    bulan = int(deadline[5:7])
    hari = int(deadline[8:10])
    selisih = (date(tahun, bulan, hari) - date.today()).days
    if selisih < 0:
        return "Terlambat " + str(-selisih) + " hari"
    elif selisih == 0:
        return "Hari ini"
    else:
        return str(selisih) + " hari lagi"


def tampilkan_tabel(judul, daftar):
    print("\n=== " + judul + " ===")
    if len(daftar) == 0:
        print("Data tidak ditemukan.")
        return
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Pelanggan", "Jenis Tugas", "Mata Kuliah", "Deadline", "Sisa Hari", "Harga", "Status"]
    for pesanan in daftar:
        # pesanan = (id, nama, jenis, matkul, deadline, harga, status)
        sisa = hitung_sisa_hari(pesanan[4], pesanan[6])
        tabel.add_row([pesanan[0], pesanan[1], pesanan[2], pesanan[3], pesanan[4], sisa, pesanan[5], pesanan[6]])
    print(tabel)