def hitung_persegi():
    print("--- Hitung Persegi ---")
    try:
        sisi = float(input("Panjang sisi: "))
    except ValueError:
        print("Input harus berupa angka!")
        return

    luas = sisi ** 2
    keliling = sisi * 4

    print(f"Luas persegi    : {luas}")
    print(f"Keliling persegi: {keliling}")


def hitung_persegi_panjang():
    print("--- Hitung Persegi Panjang ---")
    try:
        panjang = float(input("Panjang: "))
        lebar = float(input("Lebar  : "))
    except ValueError:
        print("Input harus berupa angka!")
        return

    luas = panjang * lebar
    keliling = (panjang + lebar) * 2

    print(f"Luas persegi panjang    : {luas}")
    print(f"Keliling persegi panjang: {keliling}")