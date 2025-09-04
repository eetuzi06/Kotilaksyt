luvut = [1,2,3,4,5,6,7,8,9,10,11,12]


def lista(luvut):
    eri_lista = []
    for luku in luvut:
        if luku % 2 == 0:
            eri_lista.append(luku)
    return eri_lista
karsittu = lista(luvut)

print(f"Parillisia lukuja ovat: {karsittu}")
