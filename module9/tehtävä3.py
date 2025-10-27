class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit

auto =  Auto("ABC-123", 142)
print(f"Rekisteritunnus: {auto.rekisteri}")
print(f"Huippunopeus: {auto.huippunopeus} km/h")
print(f"Nopeus: {auto.nopeus} km/h")
print(f"Matka: {auto.matka} km")

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print(f"Nopeus kiihdytysten jälkeen: {auto.nopeus} km/h")

auto.kiihdytä(-200)
print(f"Nopeus hätäjarrutuksen jälkeen: {auto.nopeus} km/h")

auto.kiihdytä(60)
print(f"Nopeus ennen ajoa: {auto.nopeus} km/h")
auto.kulje(1.5)
print(f"Kuljettu matka ajon jälkeen: {auto.matka:.1f} km")