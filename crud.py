from database import koneksi, kursor, daftar_status
from utils import (
    validasi_angka,
    input_harga,
    input_status,
    input_deadline,
    validasi_tanggal,
    cari_by_id,
    tampilkan_tabel,
)


def tambah_pesanan():
    print("\n--- Tambah Pesanan ---")
    nama = input("Nama pelanggan : ")
    jenis = input("Jenis tugas    : ")
    matkul = input("Mata kuliah    : ")
    deadline = input_deadline()
    harga = input_harga()
    status = input_status()
    kursor.execute(
        "INSERT INTO pesanan (nama, jenis, matkul, deadline, harga, status) VALUES (?, ?, ?, ?, ?, ?)",
        (nama, jenis, matkul, deadline, harga, status),
    )
    koneksi.commit()
    print("Pesanan berhasil ditambahkan!")


def lihat_pesanan():
    kursor.execute("SELECT * FROM pesanan ORDER BY id")
    hasil = kursor.fetchall()
    tampilkan_tabel("DAFTAR PESANAN", hasil)


def edit_pesanan():
    id_cari = input("Masukkan ID pesanan yang diedit: ")
    pesanan = cari_by_id(id_cari)
    if pesanan is None:
        print("ID pesanan tidak ditemukan!")
        return

    # pesanan = (id, nama, jenis, matkul, deadline, harga, status)
    nama = pesanan[1]
    jenis = pesanan[2]
    matkul = pesanan[3]
    deadline = pesanan[4]
    harga = pesanan[5]
    status = pesanan[6]

    print("Kosongkan input jika tidak ingin mengubah.")
    nama_baru = input("Nama pelanggan [" + nama + "]: ")
    jenis_baru = input("Jenis tugas [" + jenis + "]: ")
    matkul_baru = input("Mata kuliah [" + matkul + "]: ")
    deadline_baru = input("Deadline [" + deadline + "]: ")
    harga_teks = input("Harga [" + str(harga) + "]: ")
    print("Status: 1. Menunggu  2. Proses  3. Selesai")
    pilih_status = input("Status baru (1-3, kosong = tetap): ")

    if nama_baru != "":
        nama = nama_baru
    if jenis_baru != "":
        jenis = jenis_baru
    if matkul_baru != "":
        matkul = matkul_baru
    if deadline_baru != "":
        if validasi_tanggal(deadline_baru):
            deadline = deadline_baru
        else:
            print("Format deadline salah, deadline tidak diubah.")
    if harga_teks != "":
        if validasi_angka(harga_teks):
            harga = int(harga_teks)
        else:
            print("Harga tidak valid, harga tidak diubah.")
    if pilih_status == "1" or pilih_status == "2" or pilih_status == "3":
        status = daftar_status[int(pilih_status) - 1]

    kursor.execute(
        "UPDATE pesanan SET nama = ?, jenis = ?, matkul = ?, deadline = ?, harga = ?, status = ? WHERE id = ?",
        (nama, jenis, matkul, deadline, harga, status, pesanan[0]),
    )
    koneksi.commit()
    print("Pesanan berhasil diedit!")


def hapus_pesanan():
    id_cari = input("Masukkan ID pesanan yang dihapus: ")
    pesanan = cari_by_id(id_cari)
    if pesanan is None:
        print("ID pesanan tidak ditemukan!")
        return

    yakin = input("Yakin hapus pesanan " + pesanan[1] + "? (Y/T): ")
    if yakin == "Y" or yakin == "y":
        kursor.execute("DELETE FROM pesanan WHERE id = ?", (pesanan[0],))
        koneksi.commit()
        print("Pesanan berhasil dihapus!")
    else:
        print("Penghapusan dibatalkan.")