bilangan = int(input("Masukkan sebuah bilangan: "))

if bilangan % 2 == 0:
    print(bilangan, "adalah bilangan genap")
else:
    print(bilangan, "adalah bilangan ganjil")

for i in range(100):
    bilangan = int(input("Masukkan Sebuah Bilangan: "))

    if bilangan % 2 == 0:
        print(bilangan, "adalah bilangan genap")
    else:
        print(bilangan, "adalah bilangan ganjil")

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
        bilangan1 = int(input("Masukkan bilangan pertama: "))
        bilangan2 = int(input("Masukkan bilangan kedua: "))

        hasil = bilangan1 * bilangan2
        print(f"Hasil perkalian {bilangan1} x {bilangan2} = {hasil}")

        lanjut = input("Apakah ingin melakukan perkalian lain? (y/n untuk keluar): ")
        if lanjut.lower() != 'y':
            break

def kelilingpersegi():
    while True:
        sisi = float(input("Masukkan panjang sisi persegi: "))
        keliling = 4 * sisi
        print(f"Keliling persegi dengan sisi {sisi} adalah {keliling}")

        lanjut = input("Apakah ingin menghitung keliling persegi lain? (y/n untuk keluar): ")
        if lanjut.lower() != 'y':
            break

def luaspersegi():
    while True:
        sisi = float(input("Masukkan panjang sisi persegi: "))
        luas = sisi * sisi
        print(f"Luas persegi dengan sisi {sisi} adalah {luas}")

        lanjut = input("Apakah ingin menghitung luas persegi lain? (y/n untuk keluar): ")
        if lanjut.lower() != 'y':
            break
