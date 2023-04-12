while True:
    try:
        ocjena = float(input("Unesite ocjenu između 0.0 i 1.0: "))
        if ocjena < 0.0 or ocjena > 1.0:
            print("Ocjena mora biti između 0.0 i 1.0.")
        elif ocjena >= 0.9:
            print("A")
            break
        elif ocjena >= 0.8:
            print("B")
            break
        elif ocjena >= 0.7:
            print("C")
            break
        elif ocjena >= 0.6:
            print("D")
            break
        else:
            print("F")
            break
    except ValueError:
        print("Greška: Unos treba biti broj između 0.0 i 1.0")
