brojevi = []
while 1:
    unos = input("Unesite broj: ")
    if unos == 'Done':
        break
    try:
        broj = float(unos)
    except ValueError:
        print("Pogrešan unos. Unesite broj ili 'Done' za kraj unosa.")
        continue
    brojevi.append(broj)

if brojevi:
    print("Unijeli ste", len(brojevi), "brojeva.")
    print("Srednja vrijednost:", round(sum(brojevi) / len(brojevi), 2))
    print("Minimalna vrijednost:", min(brojevi))
    print("Maksimalna vrijednost:", max(brojevi))
    brojevi.sort()
    print("Sortirana lista unesenih brojeva:")
    print(brojevi)
else:
    print("Nije unesen niti jedan broj.")
