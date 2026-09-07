import ganjilgenapnew
import bangundatar
import bangunruang

def tampilkan_menu(daftar_menu):
    garis = "=" * 25
    print("\n" + garis)
    print(" MENU UTAMA")
    print(garis)
    for kode in daftar_menu:
        nama, _ = daftar_menu[kode]
        print(f"{kode}. {nama}")
    print("7. Keluar")
    print(garis)

def jalankan():
    daftar_menu = {
        "1": ("Cek Bilangan Ganjil/Genap", ganjilgenapnew.cek_bilangan),
        "2": ("Cek Bilangan Prima", ganjilgenapnew.cek_prima),
        "3": ("Hitung Persegi", bangundatar.hitung_persegi),
        "4": ("Hitung Persegi Panjang", bangundatar.hitung_persegi_panjang),
        "5": ("Hitung Kubus", bangunruang.hitung_kubus),
        "6": ("Hitung Balok", bangunruang.hitung_balok),
    }

    while True:
        tampilkan_menu(daftar_menu)
        pilihan = input("Pilih menu (1-7): ").strip()

        if pilihan == "7":
            print("Program selesai.")
            break

        if pilihan not in daftar_menu:
            print("Pilihan tidak valid, coba lagi.")
            continue

        _, fungsi = daftar_menu[pilihan]
        fungsi()

if __name__ == "__main__":
    jalankan()