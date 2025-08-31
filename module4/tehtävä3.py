luku = input("Anna luku: ")

if luku != "":
    yksi = float(luku)
    pienin = yksi
    suurin = yksi

    while True:
        luku = input("Anna luku: ")
        if luku == "":
            print("Pienin luku:", int(pienin))
            print("Suurin luku:", int(suurin))
            break
        else:
            yksi = float(luku)
            if yksi < pienin:
                pienin = yksi
            elif yksi > suurin:
                suurin = yksi

