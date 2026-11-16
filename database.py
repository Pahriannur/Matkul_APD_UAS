import sqlite3

koneksi = sqlite3.connect("joki.db")
kursor = koneksi.cursor()

daftar_status = ("Menunggu", "Proses", "Selesai")


def buat_tabel():
    kursor.execute("""
        CREATE TABLE IF NOT EXISTS pesanan (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            jenis TEXT NOT NULL,
            matkul TEXT NOT NULL,
            deadline TEXT NOT NULL,
            harga INTEGER NOT NULL,
            status TEXT NOT NULL
        )
    """)
    koneksi.commit()


def isi_data_awal():
    # isi contoh data hanya kalau tabel masih kosong
    kursor.execute("SELECT COUNT(*) FROM pesanan")
    jumlah = kursor.fetchone()[0]
    if jumlah == 0:
        contoh = [
            ("Andi", "Makalah", "Pancasila", "2026-11-20", 50000, "Proses"),
            ("Budi", "PPT", "Basis Data", "2026-11-18", 30000, "Selesai"),
            ("Citra", "Coding", "Algoritma", "2026-11-25", 75000, "Menunggu"),
        ]
        for baris in contoh:
            kursor.execute(
                "INSERT INTO pesanan (nama, jenis, matkul, deadline, harga, status) VALUES (?, ?, ?, ?, ?, ?)",
                baris,
            )
        koneksi.commit()


def tutup_koneksi():
    koneksi.close()