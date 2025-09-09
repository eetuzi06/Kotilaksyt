lentoasemat = {}
while True:
    print("\nValitse toiminto:")
    print("(1) Syötä uusi lentoasema")
    print("(2) Hae syötettyä lentoasemaa")
    print("(3) Lopeta")
    valinta = int(input("Valitse toiminto: "))
    if valinta == 1:
        koodi = input("Anna ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[koodi] = nimi
        print(f"Lentoasema {nimi}, (koodi: {koodi}) lisätty.")
    elif valinta == 2:
        koodi = input("Anna ICAO-koodi: ").upper()
        if koodi in lentoasemat:
            print(f"{koodi} = {lentoasemat[koodi]}.")
        else:
            print ("Lentoasemaa ei ole sanakirjassa.")
    elif valinta == 3:
        break

for koodi, nimi in lentoasemat.items():
    print("\nTallennetut asemat: ")
    print(f"{koodi} = {nimi}.")

