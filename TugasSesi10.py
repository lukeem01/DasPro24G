# Program Pengelola Data Mahasiswa
mahasiswa = {}

def tambah_mahasiswa():
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    jurusan = input("Masukkan Jurusan: ")
    ipk = float(input("Masukkan IPK: "))
    mahasiswa[nim] = (nama, jurusan, ipk)
    print("Mahasiswa berhasil ditambahkan.")

def tampilkan_mahasiswa():
    if not mahasiswa:
        print("Tidak ada data mahasiswa.")
    else:
        print("--- Daftar Mahasiswa ---")
        for nim, data in mahasiswa.items():
            print(f"NIM: {nim}, Nama: {data[0]}, Jurusan: {data[1]}, IPK: {data[2]}")

def cari_mahasiswa():
    nim = input("Masukkan NIM yang dicari: ")
    if nim in mahasiswa:
        data = mahasiswa[nim]
        print(f"NIM: {nim}, Nama: {data[0]}, Jurusan: {data[1]}, IPK: {data[2]}")
    else:
        print("Mahasiswa tidak ditemukan.")

def update_ipk():
    nim = input("Masukkan NIM yang akan diperbarui IPK-nya: ")
    if nim in mahasiswa:
        ipk_baru = float(input("Masukkan IPK baru: "))
        mahasiswa[nim] = (mahasiswa[nim][0], mahasiswa[nim][1], ipk_baru)
        print("IPK berhasil diperbarui.")
    else:
        print("Mahasiswa tidak ditemukan.")

def hapus_mahasiswa():
    nim = input("Masukkan NIM mahasiswa yang akan dihapus: ")
    if nim in mahasiswa:
        del mahasiswa[nim]
        print("Mahasiswa berhasil dihapus.")
    else:
        print("Mahasiswa tidak ditemukan.")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Seluruh Mahasiswa")
        print("3. Cari Mahasiswa")
        print("4. Update IPK Mahasiswa")
        print("5. Hapus Mahasiswa")
        print("6. Keluar")

        pilihan = input("Pilihan Anda: ")
        
        if pilihan == "1":
            tambah_mahasiswa()
        elif pilihan == "2":
            tampilkan_mahasiswa()
        elif pilihan == "3":
            cari_mahasiswa()
        elif pilihan == "4":
            update_ipk()
        elif pilihan == "5":
            hapus_mahasiswa()
        elif pilihan == "6":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

menu()