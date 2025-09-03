luvut = []
kys = input("Anna luku: ")

while kys != "":
    luvut.append(kys)
    kys = input("Anna luku: ")
    luvut.sort(reverse=True)
print("Viisi suurinta lukua:", luvut[:5])