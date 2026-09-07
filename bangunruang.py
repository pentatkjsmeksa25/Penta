def hitung_kubus():
    print("--- Hitung Kubus ---")
    try:
        sisi = float(input("Panjang sisi: "))
    except ValueError:
        print("Input harus berupa angka!")
        return

    volume = sisi ** 3
    luas_permukaan = 6 * sisi ** 2

    print(f"Volume kubus         : {volume}")
    print(f"Luas permukaan kubus : {luas_permukaan}")


def hitung_balok():
    print("--- Hitung Balok ---")
    try:
        panjang = float(input("Panjang: "))
        lebar = float(input("Lebar  : "))
        tinggi = float(input("Tinggi : "))
    except ValueError:
        print("Input harus berupa angka!")
        return

    sisi_sisi = [panjang * lebar, panjang * tinggi, lebar * tinggi]
    volume = panjang * lebar * tinggi
    luas_permukaan = 2 * sum(sisi_sisi)

    print(f"Volume balok         : {volume}")
    print(f"Luas permukaan balok : {luas_permukaan}")