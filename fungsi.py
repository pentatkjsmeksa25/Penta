def ganjil_genap():
    while True:
        bilangan = int(input("Masukkan sebuah bilangan: "))

        if bilangan % 2 == 0:
            print(f"{bilangan} adalah bilangan GENAP")
        else:
            print(f"{bilangan} adalah bilangan GANJIL")

        lanjut = input("Apakah ingin mengecek bilangan lain? (y/n untuk keluar): ")
        if lanjut.lower() != 'y':
            break
def perkalian():
    while True:
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
            hasil = angka1 * angka2
            print(f"Hasil perkalian {angka1} x {angka2} = {hasil}")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")
            continue

        lanjut = input("Apakah ingin melakukan perkalian lain? (y/n untuk keluar): ")
        if lanjut.lower() != 'y':
            break
def kelilingpersegi():
    while True:
        try:
            sisi = float(input("Masukkan panjang sisi persegi: "))
            keliling = 4 * sisi
            print(f"Keliling persegi dengan sisi {sisi} adalah {keliling}")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")
            continue

        lanjut = input("Apakah ingin menghitung keliling persegi lain? (y/n untuk keluar): ")
        if lanjut.lower() != 'y':
            break