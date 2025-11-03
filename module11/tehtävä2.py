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

class Sahkoauto(Auto):
    def __init__(self, rekisteri, huippunopeus, akku):
        super().__init__(rekisteri, huippunopeus)
        self.akku = akku
class Polttomoottoriauto(Auto):
    def __init__(self, rekisteri, huippunopeus, bensatankki):
        super().__init__(rekisteri, huippunopeus)
        self.bensatankki = bensatankki

sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.kiihdytä(120)
polttomoottoriauto.kiihdytä(150)

sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f"Sähköauto: {sahkoauto.rekisteri}: {sahkoauto.matka:.1f} km ajettu, nopeus {sahkoauto.nopeus} km/h, akku {sahkoauto.akku} kWh")
print(f"Polttomoottoriauto: {polttomoottoriauto.rekisteri}: {polttomoottoriauto.matka} km ajettu, nopeus {polttomoottoriauto.nopeus} km/h, tankki {polttomoottoriauto.bensatankki} l")