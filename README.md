# Sistem Pengelolaan Sewa Kost (JURAGAN CODE)

> Proyek Akhir Praktikum Dasar-Dasar Pemrograman (DDP)  
> Program Studi Sistem Informasi — Fakultas Teknik, Universitas Mulawarman (2026)

---

## 1. Judul & Tema

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
| **1** | [Dimas Surya Pasyha] | [2609116044] | [Codingan, Flowchart, Laporan, Github] |
| **2** | [Muhammad Yurcell Nabil] | [2609116073] | [Codingan, Flowchart, Laporan, Github] |
| **3** | [Arfis Orica Shirena] | [2609116076] | [Codingan, Flowchart, Laporan, Github] |
| **4** | [Fia Hulfiah] | [2609116078] | [Codingan, Flowchart, Laporan, Github] |

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

## 4. Library Python

* `json`: Membaca dan menyimpan database user atau admin dalam format JSON.
* `os`: Membersihkan tampilan layar terminal agar terminal rapi.
* `pwinput`: Menyembunyikan input password dengan karakter (***).
* `prettytable`: Menampilkan data berbentuk tabel yang rapi di terminal.
* `datetime`: Mengambil stempel waktu real-time untuk penomoran ID transaksi dan invoice.

---

## 5. Flowchart & Alur

<img width="1812" height="1032" alt="flowchart terbaru-Page-1 drawio" src="https://github.com/user-attachments/assets/114feae3-4faf-4c50-9b15-65a901ab2a04" />


Ketika program pertama kali dijalankan * `(START)`, pengguna akan di tampilkan menu Utama dengan tiga pilihan menu: Login, Registrasi, atau Keluar.

* `Proses Registrasi (Pilihan 2)`: Pengguna memasukkan username dan password baru lalu sistem langsung melakukan pengecekan ke file users.json untuk melihat apakah username tersebut sudah dipakai atau belum. Jika terdeteksi duplikat atau udah ada, sistem akan meminta pengguna untuk melakukan login ulang. Jika username belum ada, data akun baru disimpan ke users.json dan pengguna diarahkan kembali ke menu awal.

* `Proses Login (Pilihan 1)`: Pengguna memasukkan username dan password lalu sistem memverifikasi data tersebut ke file users.json.
Jika Login Gagal: Sistem memberikan batasan percobaan sebanyak 3 kali. Setiap kali gagal, kuota percobaan berkurang 1. Jika kesempatan habis (sisa == 0), sistem memberikan opsi apakah pengguna ingin kembali ke menu utama atau memilih keluar dari program.

* `Jika Login Berhasil`: Sistem mengecek role dari akun tersebut. Akun ber-role Admin akan masuk ke Menu Admin, sedangkan akun ber-role User akan masuk ke Menu User.

* `Keluar (Pilihan 3)`: Keluar dari program (END)


<img width="4812" height="1622" alt="flowchart terbaru-Halaman-2 drawio" src="https://github.com/user-attachments/assets/b21da00a-c56a-429c-8b79-0e7e83815cd7" />


* `Kelola Kamar`: Admin dapat melihat status seluruh kamar (tersedia maupun yang sudah terpakai). Di dalam sub menu ini, Admin bisa memilih dua tindakan:

* `Ubah sisa hari`: Admin memasukkan nomor kamar, sistem memvalidasi kamar, lalu Admin menginput sisa hari penyewaan yang baru sebelum disimpan ke file JSON.

* `Validasi Check-out`: Admin memasukkan nomor kamar, sistem memvalidasi kamar, lalu meminta konfirmasi checkout untuk memperbarui status kamar di file JSON.

* `Tambah Kamar`: Admin dapat menambahkan kamar baru dengan menentukan tipe kamar (L atau P) serta memilih apakah kamar tersebut fasilitas AC atau tidak. Data kamar baru ini langsung disimpan ke file JSON.

* `Lihat Saldo & Keuangan`: Admin dapat mengecek total saldo sistem yang dihitung secara otomatis dari pemasukan dan pengeluaran pada file JSON, Admin juga bisa memproses pembayaran tagihan serta mencetak invoice.

* `Hapus Akun User`: Admin melihat daftar akun user lalu memasukkan username yang ingin dihapus. Sistem akan mengecek apakah username ada di file JSON dan memverifikasi syarat penghapusan (yaitu user tidak sedang menyewa kamar dan saldonya 0). Jika syarat terpenuhi, akun berhasil dihapus.

* `Laporan Transaksi`: Admin bisa melihat seluruh riwayat transaksi yang ada di JSON atau melakukan pencarian riwayat transaksi berdasarkan username pelanggan


<img width="2022" height="1947" alt="flowchart terbaru-Halaman-3 drawio (1)" src="https://github.com/user-attachments/assets/f4119078-2a09-4162-b8c6-7c25d58126d7" />


* `Cek Info Kamar Sewaan`: program mengecek apakah akun pengguna memiliki kamar yang sedang disewa. Jika ada, sistem akan menampilkan sisa masa sewa dan sisa hari penyewaannya.

* `Melihat dan Mengisi Saldo`: Pengguna dapat melihat sisa saldo akun saat ini. Jika memilih untuk mengisi saldo, pengguna menginput nominal yang diinginkan, sistem menambah saldo, dan secara otomatis mencetak invoice transaksi.

* `Memilih Kamar yang Ingin Disewa`: Pengguna melihat daftar kamar tersedia, memilih tipe kamar (L atau P), menentukan nomor kamar, melihat daftar harga, lalu memilih durasi sewa. Sebelum memproses, sistem mengecek kecukupan saldo pengguna. Jika saldo cukup dan pengguna mengonfirmasi, transaksi diproses dan disimpan ke file JSON.

* `Memperpanjang Sewa`: Program memastikan pengguna sudah memiliki kamar sewaan. Jika punya, pengguna memasukkan durasi perpanjangan sewa. Jika saldo mencukupi, program memperbarui data sewa di file JSON dan mencetak invoice baru.

* `Logout`: Pengguna keluar dari akun dan dikembalikan ke Tampilan Utama.


---

## 6. Daftar Menu Berdasarkan Role

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

## 7. Screenshot Output & Code serta Penjelasan

## 7.1. Penjelasan output

### 7.1.1. Tampilan menu utama

<img width="443" height="178" alt="image" src="https://github.com/user-attachments/assets/96c58ec8-d041-4010-84c5-54772cb6feb0" />

Penjelasan: saat program dijalankan, sistem akan menampilkan menu utama dengan tiga pilihan, yaitu: 1. Login 2. Registrasi 3. Keluar 

### 7.1.2. Registrasi

<img width="432" height="95" alt="image" src="https://github.com/user-attachments/assets/1992f166-aa7b-490f-b13c-e876114fd2b3" />

Penjelasan: jika user memilih opsi registrasi, sistem meminta user untuk menginput username baru dan password baru. setelah itu, sistem menyimpan dalam file users.json

### 7.1.3. Login (sebagai user atau penyewa kos)

<img width="425" height="90" alt="image" src="https://github.com/user-attachments/assets/b47cd456-4e55-4328-a6a8-7060d86ac689" />

Penjelasan: setelah melakukan registrasi, user disilahkan login dengan menginput username dan password untuk dapat mengakses menu user

#### Menu user 

<img width="402" height="215" alt="image" src="https://github.com/user-attachments/assets/c4bf3e19-d94c-4af4-926b-f88b2869d791" />

Penjelasan: setelah login berhasil, sistem akan menampilkan pilihan menu sebagai berikut: 1. cek info kamar sewaan 2. melihat dan mengisi saldo 3. memilih kamar yang ingin disewakan 4. memperpanjang sewa 5. logout

#### Cek kamar yang sedang disewa

<img width="435" height="258" alt="image" src="https://github.com/user-attachments/assets/36aa55f0-ffc2-4919-9b4a-464cdff1401e" />

Penjelasan: karena caca adalah user atau penyewa baru, caca masih belum memiliki kamar 

#### Lihat dan isi saldo

<img width="453" height="428" alt="image" src="https://github.com/user-attachments/assets/7b81192f-4c16-4d2e-b284-b8f94098059d" />

Penjelasan: sebelum caca menyewa kamar, caca harus isi saldo terlebih dahulu.

#### Melihat kamar yang ingin disewa

<img width="700" height="432" alt="image" src="https://github.com/user-attachments/assets/be3dbaa7-7574-45d6-8029-944dca1988e5" />

Penjelasan: sebelum penyewa melakukan penyewaan kamar, sistem akan menampilkan tabel informasi keseluruhan kamar agar penyewa dapat melihat ketersedian kamar 

<img width="476" height="450" alt="image" src="https://github.com/user-attachments/assets/c7585865-27dd-44b6-b62e-aae03ada7a03" />

Penjelasan: setelah melihat ketersediaan kamar, penyewa dapat memilih tipe dan fasilitas yang dinginkan serta durasi sewa beserta dengan harganya. terdapat 3 pilihan yaitu: 1. 1 bulan Rp1,000,000 2. 3 bulan Rp2,800,000 3. 1 tahun Rp11,000,000

<img width="492" height="332" alt="image" src="https://github.com/user-attachments/assets/2fd9903d-8786-4fe5-b927-625cbfaae9eb" />

Penjelasan: setelah melakukan pembayaran, terdapat struk sebagai bukti telah memesan kamar

#### Perpanjangan sewa

<img width="562" height="266" alt="image" src="https://github.com/user-attachments/assets/1f24317b-4113-44d4-8e71-89b7fd14fd77" />

Penjelasan: penyewa bisa melakukan perpanjangan sewa kamar, dengan pilihan menu yaitu: 1. 1 bulan Rp1,000,000 2. 3 bulan Rp2,800,000 3. 1 tahun Rp11,000,000

<img width="840" height="328" alt="image" src="https://github.com/user-attachments/assets/2eeec1a6-af82-4f53-9920-87206b9c9b23" />

Penjelasan: setelah penyewa yakin ingin melakukan perpanjangan sewa kamar, sistem akan mencetak struknya

### 7.1.4. Login (sebagai admin atau pemilik kos)

<img width="426" height="81" alt="image" src="https://github.com/user-attachments/assets/8206443d-4afc-4027-8b28-64500d0f6e50" />

Penjelasan: admin bisa melakukan login dengan memasukkan username 'admin' dan password '123' untuk bisa mengakses menu admin

#### Menu admin

<img width="450" height="237" alt="image" src="https://github.com/user-attachments/assets/0596b9e6-4168-4a6f-81eb-39ecbcd59c05" />

Penjelasan: setelah admin berhasil login, sistem akan menampilkan menu admin yaitu: 1. Kelola kamar 2. Tambah kamar 3. Lihat saldo 4. Hapus akun 5. Laporan transaksi 6. Logout

#### Kelola kamar

<img width="672" height="393" alt="image" src="https://github.com/user-attachments/assets/68551250-b33c-4a7e-b206-2c40d9680e22" />

Penjelasan: informasi keseluruhaan kamar dapat dilhat secara lengkap oleh admin berupa tabel. lalu sistem akan menampilkan menu kelola kamar yaitu: 1. ubah sisa hari dari user 2. validasi check out 3. kembali ke menu admin

#### Ubah sisa hari sewa

<img width="635" height="217" alt="image" src="https://github.com/user-attachments/assets/9e96bf38-62fe-497d-86d3-862e959554f3" />

Penjelasan: admin atau pemilik kos dapat mengubah sisa hari penyewa kos menyewa kamar dengan menginput nomor kamar yang ingin diubah serta menginput sisa hari dari penyewa tesebut

#### Validasi checkout

<img width="593" height="90" alt="image" src="https://github.com/user-attachments/assets/2e3b9162-70f5-4958-a358-77463552ad44" />

Penjelasan: validasi checkout digunakan untuk mengubah ketersediaan kamar dalam sistem jika kamar tersebut sudah tidak ada yang menyewa

#### Tambah kamar

<img width="576" height="131" alt="image" src="https://github.com/user-attachments/assets/b886c72c-78b5-4177-942b-0485dd27d9e5" />

Penjelasan: pemilik juga dapat menambahkan unit kamar baru ke dalam sistem jika terdapat penambahan kamar kos

#### Lihat saldo 

<img width="445" height="167" alt="image" src="https://github.com/user-attachments/assets/7c7b1e7f-d31d-449a-a2ff-256a473d4ba4" />

Penjelasan: pemilik kos dapat melihat saldo atau total keuangan sekarang

### Pembayaran tagihan

<img width="436" height="386" alt="image" src="https://github.com/user-attachments/assets/8f198921-e650-41c0-b655-705976420aac" />

Penjelasan: jika pemilik memiliki pengeluaran atau tagihan yang ingin dibayar sistem meminta untuk menginput pengeluaran daan keterangan lalu sistem akan mencetak struk atau bukti transaksi

### Hapus akun

<img width="787" height="388" alt="image" src="https://github.com/user-attachments/assets/7581ab1b-63f9-49dd-9efd-503d472c25bf" />

Penjelasan: syarat admin bisa menghapus akun user adalah jika akun user tersebut tidak memiliki saaldo atau saldo Rp 0. Karena user rena masih memiliki saldo sebesar 3jt maka akun tidak bisa di hapus

### Laporan transaksi

<img width="341" height="63" alt="image" src="https://github.com/user-attachments/assets/766280f8-63ba-4917-829a-d516672ce840" />

Penjelasan: pemilik kos dapat melihat seluruh transaksi dengan 2 pilihan menu yaitu: 1. lihat seluruh transaksi 2. cari berdasarkan username

#### Lihat seluruh transaksi

<img width="797" height="588" alt="image" src="https://github.com/user-attachments/assets/67d7944b-c26e-41cb-b5dc-57de0e48dd27" />

Penjelasan: jika pemilik kos memilih menu 1 maka sistem akan menampilkan tabel seluruh transaksi 

#### Lihat transaksi berdasarkan username

<img width="642" height="228" alt="image" src="https://github.com/user-attachments/assets/ce6d9247-af3c-4503-b402-99f0ab28d3db" />

Penjelasan: jika pemilik kos memilih menu 2 maka sistem meminta untuk menginputkan username pelanggan dan sistem akan menampilkan riwayat transaaksi user atau penyewa kos itu

## 7.2. Penjelasan kode

### 7.2.1. Def file untuk penunjang file json dan penunjang def yang general

#### Pengalamatan file json

<img width="194" height="110" alt="image" src="https://github.com/user-attachments/assets/80fb4508-dd26-4ce0-b797-0369fdd47eed" />

Penjelasan: Disini kita akan memberikan nama untuk masing masing file json agar pengalamatan berhasil terbaca oleh main py kita.

#### Def load json dan save json

<img width="205" height="145" alt="image" src="https://github.com/user-attachments/assets/da46ba99-d0c1-4ea8-ae5c-e6e0650dc9ce" />

Penjelasan: Pengecekan File (os.path.exists): Program mengecek apakah file JSON tersebut sudah ada atau belum dibuat lah umpamanya. Jika file belum ada (misal saat pertama kali aplikasi dijalankan), program akan otomatis membuat file baru dengan isi data bawaan (default_data). Penanganan Error (JSONDecodeError): Jika file JSON ternyata kosong atau rusak formatnya, program tidak akan crash, melainkan aman mengembalikan nilai default_data. Lalu untuk def save_json itu pokoknya untuk nyimpen data ke file json lah misal kita habis tambah kamar atau mungkin ngelakuin tranksaksi. Mode Tulis ('w'): Membuka file target dalam mode tulis (write), yang artinya data lama di dalam file akan ditimpa dengan data terbaru yang sudah diperbarui di dalam memori program.

#### Def Catat Tranksaksi

<img width="372" height="260" alt="image" src="https://github.com/user-attachments/assets/6c1a3712-b8e6-409d-90d7-4bb8b0380fa9" />

<img width="253" height="137" alt="image" src="https://github.com/user-attachments/assets/3a2b68e1-709e-4e57-bd7e-61dbf0357a86" />

Penjelasan: Digunakan sebagai sistem "invoice berjalan" otomatis untuk merekam, membuat ID unik, menyimpan riwayat keuangan ke file transactions.json, sekaligus mencetak bukti transaksi (struk/invoice) secara real-time di terminal setiap kali ada aktivitas pembayaran. terus ada pembuatan id unik pakai kbmft lalu pakai penomoran otomatis. Terus kami pakai datetime untuk menunjukkan waktu tranksaksi aktif lah umpamanya. 

#### Def tampilkan tabel kamar

<img width="370" height="167" alt="image" src="https://github.com/user-attachments/assets/426fabde-f760-479d-8279-76f0357ae3f5" />

Penjelasan: Digunakan untuk membaca data kamar dari file rooms.json, mengurutkannya secara teratur, lalu menampilkan informasi status seluruh kamar kos ke dalam bentuk tabel terminal yang rapi menggunakan library PrettyTable. Mengembalikan Nilai (return rooms): Mengembalikan data kamar yang sudah dimuat agar bisa langsung digunakan kembali oleh fungsi lain (seperti menu pengecekan admin atau penyewaan user).

### 7.2.2. Menu utama 

### 7.2.3. Def Menu Admin

### 7.2.4. Def Menu User


## 8. File (JSON)

Sistem menggunakan 4 file JSON lokal sebagai media penyimpanan data:
* `users.json`: Menyimpan data username, password, role, dan saldo.
* `rooms.json`: Menyimpan no_kamar, tipe, status ac, status terpakai, penghuni, dan sisa_hari.
* `transactions.json`: Menyimpan riwayat id_transaksi, waktu, username, tipe, keterangan, dan jumlah.
* `prices.json`: Menyimpan tabel tarif sewa berdasarkan durasi dan fasilitas AC/Non-AC.

---


## 9. Kesimpulan & Saran

### Kesimpulan
Program Sewa Kost In berhasil menyelesaikan permasalahan pencatatan manual sewa kost. Fitur pembagian role, integrasi saldo, transaksi sewa otomatis, serta sistem penyimpanan file JSON memastikan seluruh data transaksi dan kamar aman dengan akurat.

### Saran
* Penambahan enkripsi kata sandi (misal: hashing dengan hashlib).
* Pengembangan antarmuka berbasis GUI (Graphical User Interface) atau Web.

---

## 10. Penjelasan Detail Fungsi & Struktur Kode (Code Breakdown)

Setiap fungsi dalam kode program dirancang modular untuk menangani tugas spesifik:

### A. Fungsi 
* `load_json(filename, default_data)`: Membaca file JSON dari direktori. Jika file belum ada, fungsi ini otomatis membuat file baru dengan isi data bawaan (*default*).
* `save_json(filename, data)`: Menyimpan atau memperbarui data list/dictionary Python ke dalam file berformat JSON secara terstruktur.
* `catat_transaksi(username, tipe, keterangan, jumlah)`: Mencatat transaksi keuangan secara otomatis, membuat ID unik berurutan (misal: `TRX001`, `TRX002`), menambahkan stempel waktu *real-time*, serta langsung mencetak struk/invoice ke layar terminal.

### B. Fungsi Admin (Pemilik Kost)
* `tampilkan_tabel_kamar()`: Mengambil data kamar, mengurutkan nomor kamar secara otomatis (misal: `L1`, `L2`, `P1`), dan menampilkannya dalam bentuk tabel interaktif menggunakan *PrettyTable*.
* `menu_admin_tambah_kamar()`: Menambahkan kamar baru secara dinamis. Sistem mendeteksi nomor kamar tertinggi yang ada (misal: jika sudah ada `L3`, maka otomatis membuat `L4`).
* `menu_admin_pengecekan_kamar()`: Mengubah sisa hari sewa penyewa atau melakukan proses *check-out* untuk mengosongkan status kamar.
* `menu_admin_lihat_saldo()`: Menghitung total kas dari selisih pemasukan dan pengeluaran serta mencatat pengeluaran operasional kost.
* `menu_admin_hapus_akun()`: Menghapus akun penyewa dari database setelah memvalidasi bahwa penyewa tersebut tidak memiliki sisa saldo dan tidak dalam masa sewa aktif.
* `menu_admin_laporan_transaksi()`: Menampilkan seluruh riwayat keuangan atau memfilter laporan transaksi khusus berdasarkan *username* penyewa tertentu.

### C. Fungsi User (Penyewa Kost)
* `menu_user_cek_info_sewa(username)`: Memeriksa database kamar dan menampilkan detail kamar yang sedang disewa oleh user beserta sisa hari masa sewanya.
* `menu_user_saldo(username)`: Menampilkan saldo terkini penyewa serta menyediakan fitur pengisian saldo (*top-up*).
* `menu_user_sewa_kamar(username)`: Memvalidasi agar user yang sudah menyewa tidak bisa menyewa kamar lain, menampilkan daftar kamar kosong sesuai tipe gender, menghitung kalkulasi biaya sesuai durasi, memotong saldo, dan mengaktifkan status kamar.
* `menu_user_perpanjang_sewa(username)`: Memperpanjang durasi sewa pada kamar yang sedang aktif digunakan dan menambahkan sisa hari sewa secara otomatis.

### D. Fungsi Autentikasi & Entry Point
* `login()`: Memproses autentikasi masuk dengan batas maksimal 3 kali percobaan. Pengguna diarahkan ke `main_admin_menu()` atau `main_user_menu()` sesuai hak akses (*role*).
* `registrasi()`: Mendaftarkan akun penyewa baru ke dalam file `users.json` dengan pengaman berupa pengecekan duplikasi *username*.
* `main()`: Titik awal (*entry point*) eksekusi program yang menampilkan menu utama (Login, Registrasi, Keluar) dan menangani penanganan interupsi keyboard (`Ctrl+C`).

---

## 11. Penanganan Error & Keamanan Input (Error Handling)

Untuk mencegah program *crash* saat dijalankan oleh pengguna, beberapa mekanisme penanganan error telah diterapkan:
* **Value Error Handling:** Menggunakan blok `try-except ValueError` pada setiap input angka (seperti masukan password, nominal saldo, dan pilihan menu) agar sistem tidak berhenti jika pengguna memasukkan karakter non-angka.
* **Keyboard Interrupt Handling:** Menggunakan `except KeyboardInterrupt` untuk menangkap kombinasi tombol `Ctrl+C` agar pengguna tidak bisa keluar dari program secara paksa tanpa melalui alur logout resmi.
* **Pencegahan Akun Duplikat:** Mengecek ketersediaan *username* saat registrasi untuk mencegah terjadinya *overlap* data user.
* **Validasi Hapus Akun:** Menerapkan syarat berlapis pada fitur hapus akun agar admin tidak dapat menghapus akun yang masih memiliki saldo atau masih menempati kamar.

