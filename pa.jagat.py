import json
import os
import pwinput
from prettytable import PrettyTable
from datetime import datetime

# Nama file database JSON
FILE_USERS = "users.json"
FILE_ROOMS = "rooms.json"
FILE_TRANSACTIONS = "transactions.json"
FILE_PRICES = "prices.json"

def load_json(filename, default_data):
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump(default_data, f, indent=4)
        return default_data
    with open(filename, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return default_data

def save_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def catat_transaksi(username, tipe, keterangan, jumlah):
    transactions = load_json(FILE_TRANSACTIONS, [])
    
    # Membuat ID Unik otomatis dengan pengaman jika data lama belum punya id_transaksi
    if not transactions or 'id_transaksi' not in transactions[-1]:
        id_baru = "KBMFT001"
    else:
        id_terakhir = transactions[-1]['id_transaksi']
        try:
            angka = int(id_terakhir[5:]) + 1
            id_baru = f"KBMFT{angka:03d}"
        except (ValueError, IndexError):
            id_baru = "KBMFT001"
        
    waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    new_trx = {
        "id_transaksi": id_baru,
        "waktu": waktu_sekarang,
        "username": username,
        "tipe": tipe,
        "keterangan": keterangan,
        "jumlah": jumlah
    }
    
    transactions.append(new_trx)
    save_json(FILE_TRANSACTIONS, transactions)

    # --- OTOMATIS CETAK INVOICE DI TERMINAL ---
    print("\n" + "=" * 45)
    print("          INVOICE / BUKTI TRANSAKSI          ")
    print("=" * 45)
    print(f" ID Transaksi : {new_trx['id_transaksi']}")
    print(f" Waktu        : {new_trx['waktu']}")
    print(f" Username     : {new_trx['username']}")
    print(f" Tipe         : {new_trx['tipe'].capitalize()}")
    print(f" Keterangan   : {new_trx['keterangan']}")
    print(f" Jumlah       : Rp {new_trx['jumlah']:,}")
    print("=" * 45)
    print("     Terima kasih telah menggunakan sistem!  ")
    print("=" * 45 + "\n")

def tampilkan_tabel_kamar():
    rooms = load_json(FILE_ROOMS, [])
    # Mengurutkan kamar secara otomatis (L1, L2, dst lalu P1, P2, dst)
    rooms = sorted(rooms, key=lambda x: x['no_kamar'])
    
    table = PrettyTable()
    table.field_names = ["No Kamar", "Tipe", "Fasilitas", "Status", "Penghuni", "Sisa Hari"]
    for r in rooms:
        status = "Terpakai" if r['terpakai'] else "Tersedia"
        ac_status = "AC" if r['ac'] else "Non-AC"
        penghuni = r['penghuni'] if r['penghuni'] else "-"
        sisa = f"{r['sisa_hari']} Hari" if r['terpakai'] else "-"
        table.add_row([r['no_kamar'], r['tipe'], ac_status, status, penghuni, sisa])
    
    print("\n=== INFORMASI STATUS KESELURUHAN KAMAR ===")
    print(table)
    return rooms

# --- MENU ADMIN ---
def menu_admin_tambah_kamar():
    rooms = load_json(FILE_ROOMS, [])
    print("\n--- Tambah Unit Kamar ---")
    
    # 1. Validasi Input Tipe Kamar (L/P) dengan While Loop
    while True:
        try:
            tipe = input("Input tipe kamar (L untuk Laki-laki / P untuk Perempuan): ").strip().upper()
            if tipe in ['L', 'P']:
                break # Keluar dari loop jika input sudah benar (L atau P)
            print("[!] Tipe kamar tidak valid! Harap masukkan huruf 'L' atau 'P'.")
        except KeyboardInterrupt:
            print("JANGAN KOMBINASI DENGAN CTRL!!")

    # --- CARA SEDERHANA AUTO INCREMENT NOMOR KAMAR ---
    filtered_rooms = [r for r in rooms if r['tipe'] == tipe]
    
    max_num = 0
    for r in filtered_rooms:
        try:
            angka_str = r['no_kamar'][1:] 
            angka = int(angka_str)
            if angka > max_num:
                max_num = angka
        except ValueError:
            continue
            
    no_kamar = f"{tipe}{max_num + 1}"
    print(f"Nomor kamar otomatis dibuat: {no_kamar}")
    # -----------------------------------------------

    # 2. Validasi Input AC (y/n) dengan While Loop
    while True:
        try:
            ac_input = input("Input include AC? (y/n): ").strip().lower()
            if ac_input in ['y', 'n']:
                is_ac = True if ac_input == 'y' else False
                break # Keluar dari loop jika input sudah benar (y atau n)
            print("[!] Pilihan tidak valid! Harap masukkan huruf 'y' atau 'n'.")
        except KeyboardInterrupt:
            print("JANGAN KOMBINASI DENGAN CTRL!!")
            return
        
    new_room = {
        "no_kamar": no_kamar,
        "tipe": tipe,
        "ac": is_ac,
        "terpakai": False,
        "penghuni": None,
        "sisa_hari": 0
    }
    rooms.append(new_room)
    save_json(FILE_ROOMS, rooms)
    print(f"Sukses! Kamar {no_kamar} berhasil disimpan ke file JSON.")


def menu_admin_pengecekan_kamar():
    rooms = tampilkan_tabel_kamar ()
    
    while True:
            print("\n--- Menu Kelola Kamar ---")
            print("1. Ubah sisa hari dari user")
            print("2. Validasi check out")
            print("3. Kembali ke menu admin")
            try:
                pilihan = input("Input pilihan 1-3: ")

                if pilihan == "1":
                    try:
                        no_kamar = input("\nMasukkan kamar yang ingin diubah statusnya (misal L1/P1): ").upper()
                        room = next((r for r in rooms if r['no_kamar'] == no_kamar), None)
                        
                    # --- VALIDASI JIKA KAMAR TIDAK DITEMUKAN ---
                        if room is None:
                            print(f"[ERROR] Kamar dengan nomor '{no_kamar}' tidak ditemukan di sistem!")
                            continue  # Kembali mengulang ke awal while loop
                    except KeyboardInterrupt:
                        print("JANGAN KOMBINASI DENGAN CTRL!!")

                    try:
                        sisa = int(input("Input sisa hari: "))
                        room['sisa_hari'] = sisa
                        save_json(FILE_ROOMS, rooms)
                        print("Proses penyimpanan file JSON berhasil!")
                    except ValueError:
                        print("Input hari harus angka!")
                    except KeyboardInterrupt:
                        print("JANGAN KOMBINASI DENGAN CTRL!!")
                        
                elif pilihan == "2":
                    try:
                        no_kamar = input("\nMasukkan kamar yang ingin diubah statusnya (misal L1/P1): ").upper()
                        room = next((r for r in rooms if r['no_kamar'] == no_kamar), None)
                    
                        # --- VALIDASI JIKA KAMAR TIDAK DITEMUKAN ---
                        if room is None:
                            print(f"[ERROR] Kamar dengan nomor '{no_kamar}' tidak ditemukan di sistem!")
                            continue
                    except KeyboardInterrupt:
                        print("JANGAN KOMBINASI DENGAN CTRL!!!")

                    try:# Kembali mengulang ke awal while loop
                        yakin = input("Apakah anda yakin checkout? (y/n): ").lower()
                        if yakin == 'y':
                            room['terpakai'] = False
                            room['penghuni'] = None
                            room['sisa_hari'] = 0
                            save_json(FILE_ROOMS, rooms)
                            print("Proses penyimpanan ke file JSON (Check out berhasil)!")
                        else:
                            print("Checkout dibatalkan.")
                    except KeyboardInterrupt:
                        print("JANGAN KOMBINASI DENGAN CTRL!!!")
                elif pilihan == "3":
                    break
                else:
                    print("Pilihan tidak valid!")
            except KeyboardInterrupt:
                print("JANGAN KOMBINASI DENGAN CTRL!!")

def menu_admin_lihat_saldo():
    while True:
        print("\n--- Menu Saldo Admin ---")
        print("1. Lihat saldo")
        print("2. Pembayaran tagihan")
        print("3. Kembali ke menu admin")
        try:
            pilihan = input("Input pilihan 1-3: ")
            transactions = load_json(FILE_TRANSACTIONS, [])
            if pilihan == "1":
                pemasukan = sum(t['jumlah'] for t in transactions if t['tipe'] == 'pemasukan')
                pengeluaran = sum(t['jumlah'] for t in transactions if t['tipe'] == 'pengeluaran')
                total_saldo = pemasukan - pengeluaran
                print(f"\nTotal Saldo Keuangan: Rp {total_saldo:,}")
            elif pilihan == "2":
                try:
                    bayar = int(input("Input pembayaran/pengeluaran: "))
                    ket = input("Keterangan pengeluaran: ")
                    
                    # --- UBAH BAGIAN INI ---
                    # Ganti append manual dengan memanggil catat_transaksi tipe pengeluaran
                    catat_transaksi(
                        username="admin",
                        tipe="pengeluaran",
                        keterangan=ket,
                        jumlah=bayar
                    )
                    print(f"Pengeluaran sebesar Rp {bayar:,} telah dicatat.")
                    
                except ValueError:
                    print("Nominal harus berupa angka!")
                except KeyboardInterrupt:
                    print("JANGAN KOMBINASI DENGAN CTRL!!")
            elif pilihan == "3":
                break
        except KeyboardInterrupt:
            print("JANGAN KOMBINASI DENGAN CTRL!!!")

def menu_admin_hapus_akun():
    print("\n=== MENU HAPUS AKUN PELANGGAN ===")
    users = load_json(FILE_USERS, [])
    rooms = load_json(FILE_ROOMS, [])
    
    # --- FILTER: HANYA AMBIL AKUN SELAIN ADMIN ---
    # Sesuaikan pengecekan di bawah ini dengan struktur data admin kamu 
    # (bisa berdasarkan role=='admin' atau username=='admin')
    pelanggan = [u for u in users if u.get('role') != 'admin' and u['username'] != 'admin']
    
    if not pelanggan:
        print("Belum ada data akun pelanggan terdaftar.")
        return

    # 1. Tampilkan tabel daftar seluruh pelanggan beserta saldo dan kamar aktifnya
    table = PrettyTable()
    table.field_names = ["Username", "Saldo (Rp)", "Kamar Aktif", "Status Syarat Hapus"]
    
    for u in pelanggan:
        # Cek apakah user ini sedang menyewa kamar aktif
        kamar_aktif = next((r for r in rooms if r['penghuni'] == u['username'] and r['terpakai']), None)
        
        kamar_txt = f"Kamar {kamar_aktif['no_kamar']}" if kamar_aktif else "-"
        
        # Cek status kelayakan hapus
        if u['saldo'] > 0 or kamar_aktif:
            status_hapus = "Tidak Bisa (Ada Saldo/Kamar)"
        else:
            status_hapus = "Bisa Dihapus"
            
        table.add_row([u['username'], f"{u['saldo']:,}", kamar_txt, status_hapus])
        
    print(table)
    
    # 2. Minta admin memasukkan username pelanggan yang ingin dihapus
    try:
        username_target = input("\nMasukkan username pelanggan yang ingin dihapus (atau tekan Enter untuk batal): ").strip()
    except KeyboardInterrupt:
        print("JANGAN KOMBINASI DENGAN CTRL!!")
        return
    if not username_target:
        print("Dibatalkan.")
        return
        
    # Pastikan admin tidak sengaja mengetik admin
    if username_target.lower() == 'admin':
        print("[Peringatan] Akun admin utama tidak boleh dihapus!")
        return

    # Cari data user yang dipilih dari list utama
    user = next((u for u in users if u['username'] == username_target), None)
    if not user:
        print("Akun pelanggan dengan username tersebut tidak ditemukan!")
        return
        
    kamar_aktif = next((r for r in rooms if r['penghuni'] == username_target and r['terpakai']), None)
    
    # Validasi ketat aturan penghapusan
    if user['saldo'] > 0 or kamar_aktif:
        print(f"\n[Peringatan] Akun '{username_target}' TIDAK DAPAT dihapus!")
        if user['saldo'] > 0:
            print(f"-> Pelanggan masih memiliki sisa saldo sebesar Rp {user['saldo']:,}.")
        if kamar_aktif:
            print(f"-> Pelanggan masih tercatat aktif di Kamar {kamar_aktif['no_kamar']}.")
        print("Syarat penghapusan: Saldo harus 0 dan sudah melakukan checkout kamar.")
        return
        
    # Jika syarat terpenuhi (Saldo 0 & Tidak punya kamar aktif)
    try:
        konfirmasi = input(f"\nAkun '{username_target}' memenuhi syarat. Yakin ingin menghapus permanen? (y/n): ").lower()
    except KeyboardInterrupt:
        print("JANGAN KOMBINASI DENGAN CTRL!!")
        return
    if konfirmasi == 'y':
        users = [u for u in users if u['username'] != username_target]
        save_json(FILE_USERS, users)
        print(f"Sukses! Akun dengan username '{username_target}' berhasil dihapus dari sistem.")
    else:
        print("Penghapusan akun dibatalkan.")
        
def menu_admin_laporan_transaksi():
    print("\n--- Laporan Transaksi ---")
    print("1. Lihat seluruh transaksi")
    print("2. Cari berdasarkan username")
    try:
        pilihan = input("Input pilihan 1-2: ")
    except KeyboardInterrupt:
        print("JANGAN KOMBINASI DENGAN CTRL!!")
        return
    transactions = load_json(FILE_TRANSACTIONS, [])

    if pilihan == "1":
        if not transactions:
            print("Belum ada data transaksi.")
        else:
            table = PrettyTable()
            table.field_names = ["Username", "Tipe", "Keterangan", "Jumlah (Rp)"]
            for t in transactions:
                table.add_row([t['username'], t['tipe'], t['keterangan'], f"{t['jumlah']:,}"])
            print("\n=== TABEL SELURUH TRANSAKSI ===")
            print(table)
    elif pilihan == "2":
        uname = input("Masukkan username pelanggan: ")
        filtered = [t for t in transactions if t['username'] == uname]
        if filtered:
            table = PrettyTable()
            table.field_names = ["Tipe", "Keterangan", "Jumlah (Rp)"]
            for t in filtered:
                table.add_row([t['tipe'], t['keterangan'], f"{t['jumlah']:,}"])
            print(f"\n=== RIWAYAT TRANSAKSI ({uname}) ===")
            print(table)
        else:
            print("Riwayat transaksi tidak ditemukan.")

def main_admin_menu():
    while True:
        print("\n==============================")
        print("        MENU ADMIN            ")
        print("==============================")
        print("1. Kelola kamar")
        print("2. Tambah kamar")
        print("3. Lihat saldo")
        print("4. Hapus akun")
        print("5. Laporan transaksi")
        print("6. Logout")
        try:
            pilihan = input("Input pilihan 1-6: ")
            
            if pilihan == "1":
                menu_admin_pengecekan_kamar()
            elif pilihan == "2":
                menu_admin_tambah_kamar()
            elif pilihan == "3":
                menu_admin_lihat_saldo()
            elif pilihan == "4":
                menu_admin_hapus_akun()
            elif pilihan == "5":
                menu_admin_laporan_transaksi()
            elif pilihan == "6":
                print("Logout berhasil...")
                break
            else:
                print("PILIHAN HANYA ADA 1-6 !!")
        except KeyboardInterrupt:
            print("JANGAN KOMBINASI DENGAN CTRL!!")
        

# --- MENU USER ---
def menu_user_cek_info_sewa(username):
    rooms = load_json(FILE_ROOMS, [])
    user_room = next((r for r in rooms if r['penghuni'] == username and r['terpakai']), None)
    
    # Cek dulu apakah user punya kamar atau tidak
    if user_room:
        ac_status = "AC" if user_room['ac'] else "Non-AC"
        print(f"\nKamar Anda: {user_room['no_kamar']} | Tipe: {user_room['tipe']} | Fasilitas: {ac_status} | Sisa Hari: {user_room['sisa_hari']} Hari")
    else:
        print("\nAnda belum menyewa kamar apapun.")

def menu_user_saldo(username):
    users = load_json(FILE_USERS, [])
    user = next(u for u in users if u['username'] == username)
    print(f"\nSaldo Anda saat ini: Rp {user['saldo']:,}")
    while True:
        try:
            isi = input("Isi saldo? (y/n): ").lower()
            if isi == 'y':
                try:
                    nominal = int(input("Input nominal isi saldo: "))
                    user['saldo'] += nominal
                    save_json(FILE_USERS, users)
                    
                    # --- TAMBAHKAN PEMANGGILAN CATAT TRANSAKSI DI SINI ---
                    catat_transaksi(
                        username=username,
                        tipe="pemasukan",
                        keterangan="Isi Saldo User",
                        jumlah=nominal
                    )
                    
                    print("Penambahan saldo berhasil!")
                    print(f"Saldo Anda yang Terbaru: Rp {user['saldo']:,}")
                    break
                except ValueError:
                    print("Input harus berupa angka!")
                except KeyboardInterrupt:
                    print("JANGAN KOMBINASI DENGAN CTRL!!")
            elif isi == "n":
                print("Anda tidak jadi mengisi saldo!!")
                break
            else:
                print("input hanya 'y' atau 'n'")
        except KeyboardInterrupt:
            print("JANGAN KOMBINASI DENGAN CTRL!!")

def menu_user_sewa_kamar(username):
    rooms = load_json(FILE_ROOMS, [])
    
    # Validasi: Cek apakah user sudah punya kamar aktif yang sedang disewa
    kamar_aktif = next((r for r in rooms if r['penghuni'] == username and r['terpakai']), None)
    if kamar_aktif:
        print(f"\n[Peringatan] Anda sudah terdaftar sebagai penghuni di Kamar {kamar_aktif['no_kamar']}.")
        print("Anda tidak dapat menyewa kamar lain sebelum melakukan checkout dari kamar saat ini.")
        return

    # 1. Tampilkan dulu seluruh kondisi kamar supaya user bisa lihat status & sisa hari
    tampilkan_tabel_kamar()

    prices = load_json(FILE_PRICES, {})
    users = load_json(FILE_USERS, [])
    user = next(u for u in users if u['username'] == username)
    try:
        pesan_kamar = input("Apakah anda ingin memesan kamar? (y/n): ").lower()
    except KeyboardInterrupt:
        print("JANGAN KOMBINASI DENGAN CTRL!!")
    if pesan_kamar == "y":
        while True:
            try:
                tipe = input("\nInput tipe kamar yang ingin disewa (L/P): ").upper()
            except KeyboardInterrupt:
                print("JANGAN KOMBINASI DENGAN CTRL!!")
                return
            if tipe not in ['L', 'P']:
                print("Tipe tidak valid!")
                
            else:
                # Ambil khusus kamar yang kosong (tersedia) sesuai tipe
                available_rooms = [r for r in rooms if r['tipe'] == tipe and not r['terpakai']]
                if not available_rooms:
                    print(f"Maaf, saat ini tidak ada kamar tipe {tipe} yang kosong (tersedia). Silakan cek sisa hari kamar lain di tabel atas.")

                print("\n--- Kamar Kosong yang Bisa Disewa ---")
                table_tersedia = PrettyTable()
                table_tersedia.field_names = ["No Kamar", "Fasilitas"]
                for r in available_rooms:
                    ac_txt = "AC" if r['ac'] else "Non-AC"
                    table_tersedia.add_row([r['no_kamar'], ac_txt])
                print(table_tersedia)
                try:
                    no_kamar = input("Pilih No Kamar yang ingin disewa: ").upper()
                except KeyboardInterrupt:
                    print("JANGAN KOMBINASI DENGAN CTRL!!")
                    return
                room = next((r for r in available_rooms if r['no_kamar'] == no_kamar), None)
                
                if not room:
                    print("Nomor kamar tidak valid atau tidak tersedia!")
                    return
                
                else:
                    print("\nPilih Durasi Sewa:")
                    fasilitas_key = "ac" if room['ac'] else "non_ac"
                    harga_1bln = prices["1_bulan"][fasilitas_key]
                    harga_3bln = prices["3_bulan"][fasilitas_key]
                    harga_1thn = prices["1_tahun"][fasilitas_key]

                print(f"1. 1 Bulan - Rp {harga_1bln:,}")
                print(f"2. 3 Bulan - Rp {harga_3bln:,}")
                print(f"3. 1 Tahun - Rp {harga_1thn:,}")
                try:
                    pilihan_durasi = input("Input pilihan 1-3: ")
                except KeyboardInterrupt:
                    print("JANGAN KOMBINASI DENGAN CTRL!!")
                    return
                
                durasi_mapping = {
                    "1": ("1_bulan", 30, "1 Bulan"), 
                    "2": ("3_bulan", 90, "3 Bulan"), 
                    "3": ("1_tahun", 365, "1 Tahun")
                }
                if pilihan_durasi not in durasi_mapping:
                    print("Pilihan durasi tidak valid!")
                    return

                key_durasi, jumlah_hari, label_durasi = durasi_mapping[pilihan_durasi]
                fasilitas_key = "ac" if room['ac'] else "non_ac"
                harga = prices[key_durasi][fasilitas_key]
                ac_label = "AC" if room['ac'] else "Non-AC"

                print(f"\nTotal biaya sewa ({label_durasi} - {ac_label}): Rp {harga:,}")
                if user['saldo'] < harga:
                    print("Saldo Anda tidak mencukupi untuk melakukan penyewaan ini. Silakan isi saldo terlebih dahulu.")
                    return

                konfirmasi = input("Lanjutkan pembayaran dengan saldo? (y/n): ").lower()
                if konfirmasi == 'y':
                    user['saldo'] -= harga
                    room['terpakai'] = True
                    room['penghuni'] = username
                    room['sisa_hari'] = jumlah_hari

                    save_json(FILE_USERS, users)
                    save_json(FILE_ROOMS, rooms)

                    # Dicatat sebagai pemasukan agar kas/saldo admin bertambah
                    catat_transaksi(
                        username=username,
                        tipe="pemasukan",
                        keterangan=f"Sewa kamar {room['no_kamar']} ({label_durasi})",
                        jumlah=harga
                    )
                    print(f"Berhasil! Kamar {room['no_kamar']} telah disewa selama {label_durasi}.")
                    break
                else:
                    print("Penyewaan kamar dibatalkan.")
                    break
    elif pesan_kamar == "n":
        print("Baiklah, kembali ke menu user.")

    else:
        print("Input 'y' atau 'n'!!")

def menu_user_perpanjang_sewa(username):
    rooms = load_json(FILE_ROOMS, [])
    prices = load_json(FILE_PRICES, {})
    users = load_json(FILE_USERS, [])
    
    # Cari kamar aktif yang sedang disewa oleh user ini
    user_room = next((r for r in rooms if r['penghuni'] == username and r['terpakai']), None)
    if not user_room:
        print("\nAnda tidak memiliki sewaan kamar aktif saat ini.")
        return

    user = next(u for u in users if u['username'] == username)
    ac_label = "AC" if user_room['ac'] else "Non-AC"
    
    print(f"\nKamar Saat Ini: {user_room['no_kamar']} ({ac_label}) | Sisa Hari: {user_room['sisa_hari']} Hari")
    print("\nPilih Durasi Sewa:")
    fasilitas_key = "ac" if user_room['ac'] else "non_ac"
    harga_1bln = prices["1_bulan"][fasilitas_key]
    harga_3bln = prices["3_bulan"][fasilitas_key]
    harga_1thn = prices["1_tahun"][fasilitas_key]

    print(f"1. 1 Bulan - Rp {harga_1bln:,}")
    print(f"2. 3 Bulan - Rp {harga_3bln:,}")
    print(f"3. 1 Tahun - Rp {harga_1thn:,}")
    pilihan_durasi = input("Input pilihan 1-3: ")

    durasi_mapping = {
        "1": ("1_bulan", 30, "1 Bulan"), 
        "2": ("3_bulan", 90, "3 Bulan"), 
        "3": ("1_tahun", 365, "1 Tahun")
    }
    
    if pilihan_durasi not in durasi_mapping:
        print("Pilihan durasi tidak valid!")
        return

    key_durasi, jumlah_hari, label_durasi = durasi_mapping[pilihan_durasi]
    fasilitas_key = "ac" if user_room['ac'] else "non_ac"
    harga = prices[key_durasi][fasilitas_key]

    print(f"\nTotal biaya perpanjangan ({label_durasi} - {ac_label}): Rp {harga:,}")
    print(f"Saldo Anda saat ini: Rp {user['saldo']:,}")

    if user['saldo'] < harga:
        print("Saldo Anda tidak mencukupi untuk memperpanjang sewa. Silakan isi saldo terlebih dahulu.")
        return

    konfirmasi = input("Lanjutkan pembayaran perpanjangan dengan saldo? (y/n): ").lower()
    if konfirmasi == 'y':
        # Potong saldo user
        user['saldo'] -= harga
        
        # Tambah sisa hari sewa pada kamar tersebut
        user_room['sisa_hari'] += jumlah_hari

        # Simpan perubahan ke file JSON
        save_json(FILE_USERS, users)
        save_json(FILE_ROOMS, rooms)

        # Catat ke riwayat transaksi sebagai pemasukan untuk admin
        catat_transaksi(
            username=username,
            tipe="pemasukan",
            keterangan=f"Perpanjangan sewa kamar {user_room['no_kamar']} ({label_durasi})",
            jumlah=harga
        )
        
        print(f"Berhasil! Sewa kamar {user_room['no_kamar']} berhasil diperpanjang selama {label_durasi}. Sisa hari sekarang: {user_room['sisa_hari']} hari.")
    else:
        print("Perpanjangan sewa dibatalkan.")
        
def main_user_menu(username):
    print(f"LOGIN BERHASIL, SELAMAT DATANG {username}")
    while True:
        try:
            print(f"\n==============================")
            print(f"      MENU USER ({username})  ")
            print("==============================")
            print("1. Cek info kamar sewaan")
            print("2. Melihat dan mengisi saldo")
            print("3. Memilih kamar yang ingin disewa")
            print("4. Memperpanjang sewa")
            print("5. Logout")
            pilihan = input("Input pilihan 1-5: ")

            if pilihan == "1":
                menu_user_cek_info_sewa(username)
            elif pilihan == "2":
                menu_user_saldo(username)
            elif pilihan == "3":
                menu_user_sewa_kamar(username)
            elif pilihan == "4":
                menu_user_perpanjang_sewa (username)
            elif pilihan == "5":
                print("ANDA BERHASIL LOGOUT!!")
                break
            else:
                print("PILIHAN HANYA DARI 1-5 !!")
        except KeyboardInterrupt:
            print("JANGAN KOMBINASI DENGAN CTRL")

# --- AUTENTIKASI ---
def login():

    kesempatan = 3
    for percobaan in range(1, kesempatan + 1):
        try:
            username = input("\nInput username: ")
            try:
                password = int(pwinput.pwinput(prompt="Input password: ", mask="*"))
            except ValueError:
                print("PASSWORD HARUS BERUPA ANGKA!!")
                return
            except KeyboardInterrupt:
                print("JANGAN KOMBINASI SAMA CTRL!!")
                return
        except KeyboardInterrupt:
            print("JANGAN KOMBINASI SAMA CTRL!!")
            return

        users = load_json(FILE_USERS, [])
        user = next((u for u in users if u['username'] == username and u['password'] == password), None)

        if user:
            if user['role'] == "admin":
                main_admin_menu()
                break
            else:
                main_user_menu(user['username'])
                break
        else:
            sisa = kesempatan - percobaan
            if sisa > 0:
                print(f"[ERROR] Username/Password salah! Sisa percobaan: {sisa}\n")
            else:
                print("\n[ERROR] Kesempatan login habis! Akses ditolak.")
                return False

def registrasi():
        try:
            username = input("\nInput username baru: ")
        except KeyboardInterrupt:
            print("JANGAN KOMBINASI DENGAN CTRL!!")

        try:
            password = int(pwinput.pwinput(prompt="Input password baru: ", mask="*"))
        except ValueError:
            print("Password harus berupa angka")
        except KeyboardInterrupt:
            print("jangan kombinasi dengan ctrl")
            return

        users = load_json(FILE_USERS, [])
        if any(u['username'] == username for u in users):
            print("Apakah username duplikat? Iya, Username sudah digunakan!")
            return

        new_user = {
            "username": username,
            "password": password,
            "role": "user",
            "saldo": 0
        }
        users.append(new_user)
        save_json(FILE_USERS, users)
        print("Registrasi berhasil! Silakan login.")

# --- UTAMA / ENTRY POINT ---
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("\n==============================")
        print("         TAMPILAN UTAMA       ")
        print("==============================")
        print("1. Login")
        print("2. Registrasi")
        print("3. Keluar")
        try:
            pilihan = input("Input pilihan 1-3: ")

            if pilihan == "1":
                login()
            elif pilihan == "2":
                registrasi()
            elif pilihan == "3":
                print("Terima kasih telah menggunakan sistem.")
                break
            else:
                print("Pilihan tidak valid!")
        except KeyboardInterrupt:
            print("JANGAN KOMBINASI DENGAN CTRL!!")


if __name__ == "__main__":
    main()