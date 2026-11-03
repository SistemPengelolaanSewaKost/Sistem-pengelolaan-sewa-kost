# Sistem Pengelolaan Sewa Kost (JURAGAN CODE)

> Proyek Akhir Praktikum Dasar-Dasar Pemrograman (DDP)  
> Program Studi Sistem Informasi — Fakultas Teknik, Universitas Mulawarman (2026)

---

## 1. Judul & Tema Proyek

* **Judul :** Sewa Kost In
* **Tema Utama:** Sistem Pengelolaan sewa kost
* **Mata Kuliah:** Dasar-Dasar Pemrograman (DDP)
* **Institusi:** Program Studi Sistem Informasi, Universitas Mulawarman
* **Asisten Laboratorium:**
  * Muhammad Davi Aditya Pratama (NIM. 2509116070)
  * Hanif Amelia Putri (NIM. 2509116075) 

---

## 2. Anggota Kelompok & Peran Kerja

| No | Nama Mahasiswa | NIM | Kontribusi |
| :---: | :--- | :---: | :--- |
| **1** | [Dimas Surya Pasyha] | [2609116044] | [Koordinator, Logika Program & Coding] |
| **2** | [Muhammad Yurcell Nabil] | [2609116073] | [Penyusunan Flowchart & Dokumen Laporan] |
| **3** | [Arfis Orica Shirena] | [2609116076] | [Pengembangan Fitur & Testing Bug] |
| **4** | [Fia Hulfiah] | [2609116078] | [Finishing & Dokumentasi Kode] |

---

## 3. Deskripsi & Tujuan Proyek

### Deskripsi Masalah
Pencarian dan penyewaan kamar kost di sekitar lingkungan kampus masih banyak dilakukan secara manual. Calon penyewa harus datang langsung atau menghubungi pemilik kost via pesan singkat untuk menanyakan ketersediaan kamar, harga sewa, dan fasilitas. 

Dari sisi pemilik, pencatatan data kamar, penyewa, dan pembayaran sering dilakukan di buku catatan terpisah sehingga rawan terjadi human error, data tidak diperbarui, pembayaran terlewat, atau bukti transaksi hilang.

### Rumusan Masalah
1. Bagaimana merancang aplikasi Sewa Kost In dengan fitur registrasi, login, dan pembagian hak akses (Admin vs Penyewa)?
2. Bagaimana menerapkan fungsi CRUD (Create, Read, Update, Delete) untuk mengelola data kost dan kamar?
3. Bagaimana merancang alur penyewaan kamar (pemilihan kamar, periode sewa, top-up saldo, hingga pembayaran)?
4. Bagaimana mengelola transaksi, pencatatan tagihan, dan cetak invoice secara akurat?
5. Bagaimana menyimpan seluruh data ke dalam file JSON agar data tetap persisten setelah aplikasi ditutup?

### Batasan Masalah
* Hanya memiliki 2 role pengguna: Admin (Pemilik Kost) dan User (Penyewa).
* Pembayaran dilakukan menggunakan saldo internal aplikasi (simulasi top-up), tidak terhubung ke payment gateway asli.
* Penyimpanan data menggunakan file lokal berformat JSON (users.json, rooms.json, transactions.json, prices.json).

### Tujuan Proyek
* Membangun sistem otentikasi login & registrasi terstruktur.
* Mengimplementasikan konsep CRUD penuh pada pengelolaan unit kamar.
* Menyediakan fitur transaksi otomatis (potong saldo, perpanjang sewa, dan pencetakan invoice transaksi secara otomatis).
* Memastikan seluruh perubahan data tersimpan dengan aman pada file JSON.

### Manfaat Proyek
* **Bagi Pemilik Kost:** Memudahkan pencatatan data kamar, memantau pengeluaran/pemasukan, dan mencegah kesalahan data penyewa.
* **Bagi Penyewa:** Memudahkan pengecekan kamar kosong, memilih durasi sewa transparan, serta mendapatkan bukti transaksi (invoice).

---

## 4. Analisis Teknis & Library Python

* `json`: Membaca dan menyimpan database user atau admin dalam format JSON.
* `os`: Membersihkan tampilan layar terminal agar terminal rapi.
* `pwinput`: Menyembunyikan input password dengan karakter (***).
* `prettytable`: Menampilkan data berbentuk tabel yang rapi di terminal.
* `datetime`: Mengambil stempel waktu real-time untuk penomoran ID transaksi dan invoice.

---

## 5. Flowchart & Alur Logika Sistem

<img width="1812" height="1032" alt="flowchart terbaru-Page-1 drawio" src="https://github.com/user-attachments/assets/114feae3-4faf-4c50-9b15-65a901ab2a04" />


<img width="4812" height="1622" alt="flowchart terbaru-Halaman-2 drawio" src="https://github.com/user-attachments/assets/b21da00a-c56a-429c-8b79-0e7e83815cd7" />


<img width="2022" height="1947" alt="flowchart terbaru-Halaman-3 drawio" src="https://github.com/user-attachments/assets/442ee031-0bbd-4506-90a9-4adfee9a3f13" />



---

## 6. Daftar Fitur Berdasarkan Role

### A. Hak Akses Admin (Pemilik Kost)
1. **Kelola Kamar (CRUD):** Mengubah sisa hari sewa penyewa secara manual dan melakukan validasi check-out kamar.
2. **Tambah Unit Kamar:** Penambahan nomor kamar otomatis (misal: L1, L2 untuk Laki-Laki / P1, P2 untuk Perempuan) beserta konfigurasi fasilitas (AC / Non-AC).
3. **Lihat & Kelola Saldo Kas:** Menampilkan rekapitulasi total pemasukan dan pengeluaran serta mencatat pengeluaran operasional kost.
4. **Hapus Akun Penyewa:** Validasi ketat bahwa akun penyewa hanya bisa dihapus jika saldo bernilai 0 dan status sewa sudah check-out.
5. **Laporan Transaksi:** Melihat seluruh histori transaksi keuangan dan mencari riwayat transaksi berdasarkan username penyewa.

### B. Hak Akses User (Penyewa Kost)
1. **Cek Info Kamar Sewaan:** Menampilkan informasi unit kamar yang sedang disewa, fasilitas, dan sisa hari sewa.
2. **Melihat & Mengisi Saldo:** Menampilkan saldo saat ini dan melakukan pengisian saldo (top-up).
3. **Pilih & Sewa Kamar:** Memilih tipe kamar (L/P), melihat kamar kosong, memilih durasi sewa (1 Bulan, 3 Bulan, atau 1 Tahun), serta melakukan pembayaran otomatis yang memotong saldo dan mencetak invoice.
4. **Perpanjang Masa Sewa:** Memperpanjang durasi sewa kamar aktif tanpa perlu check-out.

---

## 7. Output Terminal & Penjelasan Kode

### Contoh Tampilan Struk / Invoice Transaksi di Terminal:
=============================================
             TRANSAKSI / INVOICE             
=============================================
 ID Transaksi : TRX001
 Waktu        : 2026-10-29 10:15:30
 Username     : yurcell
 Tipe         : Pemasukan
 Keterangan   : Sewa kamar L1 (1 Bulan)
 Jumlah       : Rp 800,000
=============================================
 Terima kasih telah menggunakan sistem!
=============================================

### Contoh Tabel Informasi Status Keseluruhan Kamar:
=== INFORMASI STATUS KESELURUHAN KAMAR ===
+----------+------+-----------+-----------+----------+-----------+
| No Kamar | Tipe | Fasilitas |   Status  | Penghuni | Sisa Hari |
+----------+------+-----------+-----------+----------+-----------+
|    L1    |  L   |     AC    | Terpakai  | yurcell  |  30 Hari  |
|    L2    |  L   |   Non-AC  | Tersedia  |    -     |     -     |
|    P1    |  P   |     AC    | Tersedia  |    -     |     -     |
+----------+------+-----------+-----------+----------+-----------+

---

## 8. Struktur File Database (JSON)

Sistem menggunakan 4 file JSON lokal sebagai media penyimpanan data:
* `users.json`: Menyimpan data username, password, role, dan saldo.
* `rooms.json`: Menyimpan no_kamar, tipe, status ac, status terpakai, penghuni, dan sisa_hari.
* `transactions.json`: Menyimpan riwayat id_transaksi, waktu, username, tipe, keterangan, dan jumlah.
* `prices.json`: Menyimpan tabel tarif sewa berdasarkan durasi dan fasilitas AC/Non-AC.

---

## 9. Cara Menjalankan Program

1. Clone Repositori ini:
   `git clone https://github.com/USERNAME/Sewa-Kost-In.git`
   `cd Sewa-Kost-In`

2. Install Dependensi Tambahan:
   `pip install prettytable pwinput`

3. Jalankan Aplikasi:
   `python main.py`

---

## 10. Kesimpulan & Saran

### Kesimpulan
Aplikasi Sewa Kost In berhasil menyelesaikan permasalahan pencatatan manual sewa kost. Fitur pembagian role, integrasi saldo, transaksi sewa otomatis, serta sistem penyimpanan file JSON memastikan seluruh data transaksi dan kamar terorganisir dengan akurat.

### Saran
* Penambahan enkripsi kata sandi (misal: hashing dengan hashlib).
* Pengembangan antarmuka berbasis GUI (Graphical User Interface) atau Web.

---

## 11. Penjelasan Detail Fungsi & Struktur Kode (Code Breakdown)

Setiap fungsi dalam kode program dirancang modular untuk menangani tugas spesifik:

### A. Fungsi Database & Utility
* `load_json(filename, default_data)`: Membaca file JSON dari direktori. Jika file belum ada, fungsi ini otomatis membuat file baru dengan isi data bawaan (*default*).
* `save_json(filename, data)`: Menyimpan atau memperbarui data list/dictionary Python ke dalam file berformat JSON secara terstruktur.
* `catat_transaksi(username, tipe, keterangan, jumlah)`: Mencatat transaksi keuangan secara otomatis, membuat ID unik berurutan (misal: `TRX001`, `TRX002`), menambahkan stempel waktu *real-time*, serta langsung mencetak struk/invoice ke layar terminal.

### B. Fungsi Manajemen Admin (Pemilik Kost)
* `tampilkan_tabel_kamar()`: Mengambil data kamar, mengurutkan nomor kamar secara otomatis (misal: `L1`, `L2`, `P1`), dan menampilkannya dalam bentuk tabel interaktif menggunakan *PrettyTable*.
* `menu_admin_tambah_kamar()`: Menambahkan kamar baru secara dinamis. Sistem mendeteksi nomor kamar tertinggi yang ada (misal: jika sudah ada `L3`, maka otomatis membuat `L4`).
* `menu_admin_pengecekan_kamar()`: Mengubah sisa hari sewa penyewa atau melakukan proses *check-out* untuk mengosongkan status kamar.
* `menu_admin_lihat_saldo()`: Menghitung total kas dari selisih pemasukan dan pengeluaran serta mencatat pengeluaran operasional kost.
* `menu_admin_hapus_akun()`: Menghapus akun penyewa dari database setelah memvalidasi bahwa penyewa tersebut tidak memiliki sisa saldo dan tidak dalam masa sewa aktif.
* `menu_admin_laporan_transaksi()`: Menampilkan seluruh riwayat keuangan atau memfilter laporan transaksi khusus berdasarkan *username* penyewa tertentu.

### C. Fungsi Operasional User (Penyewa Kost)
* `menu_user_cek_info_sewa(username)`: Memeriksa database kamar dan menampilkan detail kamar yang sedang disewa oleh user beserta sisa hari masa sewanya.
* `menu_user_saldo(username)`: Menampilkan saldo terkini penyewa serta menyediakan fitur pengisian saldo (*top-up*).
* `menu_user_sewa_kamar(username)`: Memvalidasi agar user yang sudah menyewa tidak bisa menyewa kamar lain, menampilkan daftar kamar kosong sesuai tipe gender, menghitung kalkulasi biaya sesuai durasi, memotong saldo, dan mengaktifkan status kamar.
* `menu_user_perpanjang_sewa(username)`: Memperpanjang durasi sewa pada kamar yang sedang aktif digunakan dan menambahkan sisa hari sewa secara otomatis.

### D. Fungsi Autentikasi & Entry Point
* `login()`: Memproses autentikasi masuk dengan batas maksimal 3 kali percobaan. Pengguna diarahkan ke `main_admin_menu()` atau `main_user_menu()` sesuai hak akses (*role*).
* `registrasi()`: Mendaftarkan akun penyewa baru ke dalam file `users.json` dengan pengaman berupa pengecekan duplikasi *username*.
* `main()`: Titik awal (*entry point*) eksekusi program yang menampilkan menu utama (Login, Registrasi, Keluar) dan menangani penanganan interupsi keyboard (`Ctrl+C`).

---

## 12. Penanganan Error & Keamanan Input (Error Handling)

Untuk mencegah program *crash* saat dijalankan oleh pengguna, beberapa mekanisme penanganan error telah diterapkan:
* **Value Error Handling:** Menggunakan blok `try-except ValueError` pada setiap input angka (seperti masukan password, nominal saldo, dan pilihan menu) agar sistem tidak berhenti jika pengguna memasukkan karakter non-angka.
* **Keyboard Interrupt Handling:** Menggunakan `except KeyboardInterrupt` untuk menangkap kombinasi tombol `Ctrl+C` agar pengguna tidak bisa keluar dari program secara paksa tanpa melalui alur logout resmi.
* **Pencegahan Akun Duplikat:** Mengecek ketersediaan *username* saat registrasi untuk mencegah terjadinya *overlap* data user.
* **Validasi Hapus Akun:** Menerapkan syarat berlapis pada fitur hapus akun agar admin tidak dapat menghapus akun yang masih memiliki saldo atau masih menempati kamar.

