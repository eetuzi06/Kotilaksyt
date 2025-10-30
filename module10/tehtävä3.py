class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.nyky = alinkerros  # hissi aloittaa alimmasta kerroksesta

    def kerros_ylös(self):
        if self.nyky < self.ylinkerros:
            self.nyky += 1
            print(f"Hissi on nyt kerroksessa {self.nyky}")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    def kerros_alas(self):
        if self.nyky > self.alinkerros:
            self.nyky -= 1
            print(f"Hissi on nyt kerroksessa {self.nyky}")
        else:
            print("Hissi on jo alimmassa kerroksessa.")

    def siirry_kerrokseen(self, kerros):
        print(f"Siirrytään kerrokseen {kerros}")
        if kerros > self.nyky:
            while self.nyky < kerros:
                self.kerros_ylös()
        elif kerros < self.nyky:
            while self.nyky > kerros:
                self.kerros_alas()
        else:
            print("Hissi on jo kyseisessä kerroksessa.")


class Talo:
    def __init__(self, alinkerros, ylinkerros, hissien_lkm):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.hissit = [Hissi(alinkerros, ylinkerros) for _ in range(hissien_lkm)]
        print(f"Talo luotu, jossa {hissien_lkm} hissiä kerroksissa {alinkerros}-{ylinkerros}.")

    def aja_hissiä(self, hissin_numero, kerros):
        if 1 <= hissin_numero <= len(self.hissit):
            print(f"\nAjetaan hissiä {hissin_numero} kerrokseen {kerros}")
            hissi = self.hissit[hissin_numero - 1]
            hissi.siirry_kerrokseen(kerros)
        else:
            print("Virheellinen hissin numero.")

    def palohälytys(self):
        print("PALOHÄLYTYS! Kaikki hissit siirtyvät alimpaan kerrokseen!")
        for i in range(len(self.hissit)):
            print(f"\nHissi {i + 1}:")
            hissi = self.hissit[i]
            hissi.siirry_kerrokseen(self.alinkerros)



talo = Talo(1, 10, 3)
talo.aja_hissiä(1, 5)
talo.aja_hissiä(2, 7)
talo.aja_hissiä(3, 3)

talo.palohälytys()
