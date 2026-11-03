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

Penjelasan: saat program dijalankan, sistem akan menampilkan menu utama dengan tiga pilihan, yaitu: 
1. Login
2. Registrasi
3. Keluar 

### 7.1.2. Registrasi

<img width="432" height="95" alt="image" src="https://github.com/user-attachments/assets/1992f166-aa7b-490f-b13c-e876114fd2b3" />

Penjelasan: jika user memilih opsi registrasi, sistem meminta user untuk menginput username baru dan password baru. setelah itu, sistem menyimpan dalam file users.json


### 7.1.3. Login (sebagai user atau penyewa kos)

<img width="425" height="90" alt="image" src="https://github.com/user-attachments/assets/b47cd456-4e55-4328-a6a8-7060d86ac689" />

Penjelasan: setelah melakukan registrasi, user disilahkan login dengan menginput username dan password untuk dapat mengakses menu user


#### Menu user 

<img width="402" height="215" alt="image" src="https://github.com/user-attachments/assets/c4bf3e19-d94c-4af4-926b-f88b2869d791" />

Penjelasan: setelah login berhasil, sistem akan menampilkan pilihan menu sebagai berikut:
1. cek info kamar sewaan
2. melihat dan mengisi saldo
3. memilih kamar yang ingin disewakan
4. memperpanjang sewa
5. logout


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

Penjelasan: setelah melihat ketersediaan kamar, penyewa dapat memilih tipe dan fasilitas yang dinginkan serta durasi sewa beserta dengan harganya. terdapat 3 pilihan yaitu: 
1. 1 bulan Rp1,000,000
2. 3 bulan Rp2,800,000
3. 1 tahun Rp11,000,000

<img width="492" height="332" alt="image" src="https://github.com/user-attachments/assets/2fd9903d-8786-4fe5-b927-625cbfaae9eb" />

Penjelasan: setelah melakukan pembayaran, terdapat struk sebagai bukti telah memesan kamar


#### Perpanjangan sewa

<img width="562" height="266" alt="image" src="https://github.com/user-attachments/assets/1f24317b-4113-44d4-8e71-89b7fd14fd77" />

Penjelasan: penyewa bisa melakukan perpanjangan sewa kamar, dengan pilihan menu yaitu: 
1. 1 bulan Rp1,000,000
2. 3 bulan Rp2,800,000
3. 1 tahun Rp11,000,000


<img width="840" height="328" alt="image" src="https://github.com/user-attachments/assets/2eeec1a6-af82-4f53-9920-87206b9c9b23" />

Penjelasan: setelah penyewa yakin ingin melakukan perpanjangan sewa kamar, sistem akan mencetak struknya


### 7.1.4. Login (sebagai admin atau pemilik kos)

<img width="426" height="81" alt="image" src="https://github.com/user-attachments/assets/8206443d-4afc-4027-8b28-64500d0f6e50" />

Penjelasan: admin bisa melakukan login dengan memasukkan username 'admin' dan password '123' untuk bisa mengakses menu admin


#### Menu admin

<img width="450" height="237" alt="image" src="https://github.com/user-attachments/assets/0596b9e6-4168-4a6f-81eb-39ecbcd59c05" />

Penjelasan: setelah admin berhasil login, sistem akan menampilkan menu admin yaitu: 
1. Kelola kamar
2. Tambah kamar
3. Lihat saldo
4. Hapus akun
5. Laporan transaksi
6. Logout


#### Kelola kamar

<img width="672" height="393" alt="image" src="https://github.com/user-attachments/assets/68551250-b33c-4a7e-b206-2c40d9680e22" />

Penjelasan: informasi keseluruhaan kamar dapat dilhat secara lengkap oleh admin berupa tabel. lalu sistem akan menampilkan menu kelola kamar yaitu: 
1. ubah sisa hari dari user
2. validasi check out
3. kembali ke menu admin


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

Penjelasan: pemilik kos dapat melihat seluruh transaksi dengan 2 pilihan menu yaitu: 
1. lihat seluruh transaksi
2. cari berdasarkan username


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

#### Def login

<img width="418" height="335" alt="image" src="https://github.com/user-attachments/assets/ebce92c0-2616-43a9-8e55-6069181b3617" />

Penjelasan: Mengelola sistem otentikasi masuk (login) bagi multi-role (Admin dan User) dengan batasan kesempatan mencoba untuk alasan keamanan. Lalu disitu kami pakai library pwinput supaya ketika kita input password akan dilambangkan dengan bintang *. Lalu untuk password kami pakai tipe data int, jadi password hanya berupa angka. Pengguna diberikan batas maksimal 3 kali percobaan salah sebelum akses dikunci.

#### Def Registrasi

<img width="319" height="272" alt="image" src="https://github.com/user-attachments/assets/b972df07-3150-4327-9c26-8434ad11eef2" />

Penjelasan: pendaftaran akun baru bagi pengguna (user) ke dalam sistem. Mengecek ke file users.json apakah username tersebut sudah pernah terdaftar sebelumnya untuk mencegah duplikasi akun. Jika aman, data akun baru dibuat dengan peran bawaan (role: "user") dan saldo awal bernilai 0, lalu disimpan secara permanen menggunakan save_json.

#### Def Main

<img width="248" height="265" alt="image" src="https://github.com/user-attachments/assets/11d09de2-ec47-47ee-90bb-f9fc5c3f5ee3" />

Penjelasan: Disini kita pakai os clear supaya tampilan dari terminal itu bersih. Lalu menggunakan perulangan while True yang menjadi perulangan utama dari sistem kami

### 7.2.3. Def Menu Admin

#### Def tambah_kamar

<img width="410" height="289" alt="image" src="https://github.com/user-attachments/assets/71c21428-11f8-4907-9410-4e4342b591c8" />
<img width="287" height="250" alt="image" src="https://github.com/user-attachments/assets/e8cc272c-dd6e-4032-9354-f7b2fd8453a4" />

Penjelasan: Digunakan oleh admin untuk menambahkan unit kamar kos baru ke dalam sistem secara interaktif dengan penomoran otomatis dan validasi input yang aman. Sistem menyaring kamar berdasarkan tipenya, mencari nomor urut angka terbesar yang sudah ada, lalu secara otomatis menaikkan angkanya (misal: jika kamar L terakhir adalah L3, maka otomatis dibuatkan L4). Menyusun data kamar baru ke dalam struktur dictionary (dengan status awal belum terpakai/False, belum ada penghuni, dan sisa hari 0), lalu menyimpannya secara permanen ke file rooms.json menggunakan fungsi save_json.

#### Def Admin_Pengecekan_kamar

<img width="431" height="311" alt="image" src="https://github.com/user-attachments/assets/11d94bd4-d1f1-4a9e-bd47-4f94bb5d3f56" />
<img width="409" height="305" alt="image" src="https://github.com/user-attachments/assets/a65d27f6-0ad1-4200-8551-c211a3e25fae" />

Penjelasan: Digunakan oleh admin untuk mengelola status operasional kamar kos secara berkala, yang meliputi pengubahan sisa masa sewa penghuni dan validasi proses checkout kamar. Memanggil fungsi tampilkan_tabel_kamar(). Pakai while true untuk perulangan dari sub menu di kelola kamar. Mengubah nilai sisa_hari sesuai input angka admin, lalu langsung memperbarui file rooms.json. Mengubah status kamar menjadi kosong (terpakai = False), menghapus data penghuni (penghuni = None), mereset sisa hari menjadi 0, dan menyimpan perubahannya

#### Def menu

<img width="422" height="341" alt="image" src="https://github.com/user-attachments/assets/97bb0f4b-4784-4c3a-ac7d-bc30427e7d17" />

Penjelasan: Digunakan oleh admin untuk memantau total saldo keuangan kos secara real-time serta mencatat transaksi pengeluaran operasional (seperti pembayaran tagihan). Pakai while True untuk perulangan dari sub menu nya. Memuat seluruh data transaksi dari file transactions.json, lalu menjumlahkan total seluruh transaksi yang bertipe "pemasukan" dan menguranginya dengan total transaksi bertipe "pengeluaran" untuk mendapatkan nominal saldo akhir yang akurat

#### Def Menu_Hapus_akun

<img width="416" height="299" alt="image" src="https://github.com/user-attachments/assets/c8853a0d-2512-4b60-9581-325a15cd2ddd" />

<img width="433" height="302" alt="image" src="https://github.com/user-attachments/assets/9aa1f439-ef93-48f3-bbd8-094f57763a53" />

<img width="428" height="168" alt="image" src="https://github.com/user-attachments/assets/a65e7cb7-20e1-4c1c-a00c-ebe12e9d5b43" />

Penjelasan: Memuat data dari users.json dan menyaring akun agar hanya menampilkan daftar pengguna umum (user), sehingga akun admin utama terlindungi. Tabel Status Pelanggan (PrettyTable): Menampilkan daftar akun lengkap dengan informasi saldo tersisa, status kamar aktif, serta keterangan kelayakan apakah akun tersebut sudah bisa dihapus atau belum. if user['saldo'] > 0 or kamar_aktif itu untuk Mencegah penghapusan akun jika pelanggan yang bersangkutan masih memiliki sisa saldo aktif di dompet digitalnya atau masih tercatat menghuni kamar kos (wajib bersyarat saldo 0 dan sudah checkout).

#### Def menu_laporan_tranksaksi

<img width="409" height="316" alt="image" src="https://github.com/user-attachments/assets/0a630de5-dba3-4383-b81d-45566d5f56c1" />

Penjelasan: Digunakan oleh admin untuk memantau, merekap, dan mencari riwayat laporan arus keuangan (transaksi masuk dan keluar) yang tersimpan di dalam sistem. Memuat seluruh data transaksi secara otomatis dari file transactions.json menggunakan fungsi load_json. Opsi 1 (Seluruh Transaksi): Menampilkan seluruh riwayat arus kas ke dalam tabel terminal yang rapi menggunakan PrettyTable lengkap dengan informasi username, tipe transaksi, keterangan, dan nominal uangnya.   Opsi 2 (Pencarian Berdasarkan Username): Melakukan penyaringan data transaksi berdasarkan nama pengguna (username) yang diinputkan oleh admin, sehingga riwayat pembayaran dari penghuni tertentu bisa dilacak dengan mudah dan cepat.

#### Def Menu_admin

<img width="267" height="298" alt="image" src="https://github.com/user-attachments/assets/422e327a-f68d-4512-8698-2b4f24ae4eac" />

Penjelasan: jadi disini kita tinggal menggunakan while True sebagai perulangan utama di menu admin, lalu menggunakan logika if elif else. Lalu kita tinggal memanggil setiap fungsi/def yang telah kita buat sebelumnya.

### 7.2.4. Def Menu User

<img width="848" height="418" alt="Screenshot 2026-11-03 201252" src="https://github.com/user-attachments/assets/c21a003e-ed4d-4a41-a9f6-86c17edfac86" />

1. Definisi fungsi: `main_user_menu(username)` adalah fungsi menu utama, dan username dipakai agar menu bisa menampilkan nama user yang sedang login.   
2. Pesan sambutan: Program mencetak “LOGIN BERHASIL, SELAMAT DATANG” plus nama user lewat `f-string`. Pesan ini muncul sekali saja karena ada di luar perulangan.
3. Perulangan `while True`: Membuat menu muncul terus-menerus, jadi user bisa pilih fitur berkali-kali tanpa login ulang, sampai ia memilih untuk logout.
4. Blok `try`: Dipakai untuk menangkap error, misalnya kalau user ngetik huruf padahal diminta angka, supaya program nggak langsung crash.
5. Tampilan menu: Baris print dengan tanda = bikin header menu tampil rapi, dan \n nambah baris kosong di atasnya.
7. Lima pilihan menu: Cek info kamar sewaan, lihat dan isi saldo, pilih kamar yang mau disewa, perpanjang sewa, dan logout.
8. Input pilihan: `input()` meminta user mengetik angka 1-5 dan hasilnya disimpan di variabel pilihan. Hasilnya bertipe string, jadi kalau mau dibandingkan sebagai angka perlu diubah terlebuh dahulu pakai `int()`.

<img width="1273" height="481" alt="Screenshot 2026-11-03 211302" src="https://github.com/user-attachments/assets/64ee040b-fb18-4305-9132-d0ac49aab304" />

1. Percabangan `if-elif`: Variabel pilihan dari input() akan dicek satu per satu. Karena input() hasilnya string, pembandingnya ditulis "1", "2", dst. (pakai tanda kutip), jadi tidak perlu int().
2. Pilihan 1-4: Masing-masing memanggil fungsi lain dan mengirim username sebagai argumen: `menu_user_cek_info_sewa`, `menu_user_saldo`, `menu_user_sewa_kamar`, dan `menu_user_perpanjang_sewa`. Jadi setiap fitur dipisah ke fungsinya sendiri agar kodenya rapi dan gampang dikelola.
3. Pilihan 5 (logout): Program mencetak “ANDA BERHASIL LOGOUT!!” lalu break. Ini yang menghentikan `while True`, sehingga user keluar dari menu.
4. Blok `else`: Kalau input bukan 1 sampai 5 (misalnya “9” atau huruf), program menampilkan “PILIHAN HANYA DARI 1-5 !!” lalu menu muncul lagi karena masih di dalam perulangan.
5. `except KeyboardInterrupt`: Ini merupakan pasangan dari try. Kalau user menekan Ctrl+C, program tidak langsung berhenti, tapi menampilkan pesan “JANGAN KOMBINASI DENGAN CTRL” dan menu tetap lanjut.

<img width="1396" height="626" alt="Screenshot 2026-11-03 211808" src="https://github.com/user-attachments/assets/0851ecf4-946d-4e0c-8434-f4d0d16e2bbd" />

1. Batas percobaan: Fungsi `login()` menetapkan kesempatan = 3, dan perulangan for dengan range(1, kesempatan + 1) membatasi pengguna maksimal tiga kali percobaan.
2. `Input username`: Username diminta lewat `input()`, dengan \n untuk memberi baris kosong agar tampilan rapi.
3. `Input password`: `pwinput.pwinput()` menyamarkan ketikan menjadi *, lalu hasilnya dikonversi dengan `int()` sehingga password harus berupa angka.
4. Penanganan `ValueError`: Jika password bukan angka, konversi gagal, program menampilkan pesan peringatan, lalu keluar dari fungsi dengan `return`.
5. Penanganan `KeyboardInterrupt`: Dua blok (baris 670 dan 673) menangani penekanan Ctrl+C pada `input password` dan `username`, dengan menampilkan peringatan lalu keluar dari fungsi.
6. Pengambilan data: `load_json(FILE_USERS, [])` membaca data pengguna dari file JSON, dengan [] sebagai nilai default jika file kosong atau belum ada.
7. Pencarian pengguna: `next()` dengan generator expression mengambil data pertama yang username dan password-nya cocok, atau None jika tidak ada.

<img width="1283" height="443" alt="Screenshot 2026-11-03 212544" src="https://github.com/user-attachments/assets/073c1771-9d5f-45ad-a272-a08f28c3a213" />

1. Pengecekan hasil pencarian: `if user:` bernilai benar apabila data pengguna ditemukan pada pencarian sebelumnya. Jika hasilnya None, program masuk ke blok else.
2. Pengecekan peran admin: Jika `user['role']` bernilai "admin", program memanggil `main_admin_menu()` lalu `break` untuk menghentikan perulangan percobaan login.
3. Pengguna biasa: Jika perannya bukan admin, program memanggil `main_user_menu(user['username'])` dengan username sebagai argumen, kemudian break.
4. Login gagal: Pada blok `else` terluar, variabel sisa dihitung dari kesempatan - percobaan, yaitu jumlah percobaan yang masih tersisa.
5. Masih ada kesempatan: Jika sisa > 0, program menampilkan pesan kesalahan beserta jumlah sisa percobaan, lalu perulangan berlanjut ke percobaan berikutnya.
6. Kesempatan habis: Jika sisa sudah 0, program menampilkan pesan bahwa akses ditolak, lalu `return False` untuk mengakhiri fungsi dengan status gagal.

<img width="1381" height="567" alt="Screenshot 2026-11-03 213609" src="https://github.com/user-attachments/assets/1296efb3-d609-4ad6-9834-e00a4cbd9e43" />

1. Input username: Username baru diminta lewat input() di dalam blok try. Jika pengguna menekan Ctrl+C, program menampilkan peringatan.
2. Input password: `pwinput.pwinput()` menyamarkan ketikan menjadi *, lalu hasilnya dikonversi dengan int() sehingga password harus berupa angka.
3. Penanganan ValueError: Jika password bukan angka, konversi gagal dan program menampilkan pesan peringatan. Pada bagian ini tidak ada return, jadi eksekusi tetap berlanjut.
Penanganan `KeyboardInterrupt` pada password: Program menampilkan peringatan lalu keluar dari fungsi dengan return.
5. Pengambilan data: `load_json(FILE_USERS, [])` membaca daftar pengguna yang sudah terdaftar, dengan [] sebagai nilai default jika file kosong atau belum ada.
6. Pengecekan username duplikat: any() dengan generator expression memeriksa apakah ada pengguna yang username-nya sama dengan input. Jika ada, program menampilkan pesan bahwa username sudah digunakan, lalu keluar dari fungsi dengan return.

<img width="1028" height="316" alt="Screenshot 2026-11-03 215619" src="https://github.com/user-attachments/assets/bbf80e68-9b84-48c6-8597-54ef2b63b00b" />

1. Pembuatan data pengguna: Dictionary `new_user` menyimpan empat data: username dan password dari input sebelumnya, role yang diset "user", dan saldo dengan nilai awal 0.
2. Penetapan peran otomatis: Karena role ditulis langsung sebagai "user", setiap akun hasil registrasi pasti berperan sebagai pengguna biasa. Akun admin tidak bisa dibuat lewat fitur ini.
3. Penambahan ke daftar: `users.append(new_user)` menambahkan data baru ke daftar pengguna yang tadi dibaca dari file JSON.
4. Penyimpanan ke file: `save_json(FILE_USERS, users)` menulis daftar yang sudah diperbarui kembali ke file JSON, sehingga akun tersimpan permanen.
5. Konfirmasi: Program menampilkan pesan bahwa registrasi berhasil dan pengguna dapat langsung login.


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

