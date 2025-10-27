class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

auto =  Auto("ABC-123", 142)
print(f"Rekisteritunnus: {auto.rekisteri}")
print(f"Huippunopeus: {auto.huippunopeus} km/h")
print(f"Nopeus: {auto.nopeus} km/h")
print(f"Matka: {auto.matka} km")

