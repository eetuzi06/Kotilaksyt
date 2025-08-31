yritys = 0

while yritys < 5:
    kys1 = input("Anna käyttäjätunnus: ")
    kys2 = input("Anna salasana: ")
    if kys1 == "python" and kys2 == "rules)":
        print("Tervetuloa!")
        break
    else:
        yritys = yritys + 1

else:
    print("Pääsy evätty.")




