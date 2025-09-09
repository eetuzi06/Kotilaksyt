joukko = set()
kysymys = input("Anna nimi: ")

while kysymys != "":

    if kysymys in joukko:
        print("Aiemmin syötetty nimi.")
    else:
        joukko.add(kysymys)
        print("Uusi nimi.")
    kysymys = input("Anna nimi: ")

print("\nSyötetyt nimet: ")

for nimi in joukko:
    print(nimi)


