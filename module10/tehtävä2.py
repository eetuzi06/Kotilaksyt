class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nyky = alin

    def kerros_ylös(self):
        if self.nyky < self.ylin:
            self.nyky += 1
            print(f"Hissi on nyt kerroksessa {self.nyky}")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")
    def kerros_alas(self):
        if self.nyky > self.alin:
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
    def __init__(self, alin, ylin, hissien_lkm):
        if alin > ylin:
            alin, ylin = ylin, alin
        self.alinkerros = alin
        self.ylinkerros = ylin
        self.hissit = [Hissi(self.alinkerros, self.ylinkerros) for _ in range(hissien_lkm)]
        print(f"Talo luotu, jossa {len(self.hissit)} hissiä kerroksissa {self.alinkerros}-{self.ylinkerros}.")

    def aja_hissiä(self, hissin_numero, kerros):
        if 1 <= hissin_numero <= len(self.hissit):
            print(f"\nAjetaan hissiä {hissin_numero} kerrokseen {kerros}:")
            hissi = self.hissit[hissin_numero - 1]
            hissi.siirry_kerrokseen(kerros)
        else:
            print("Virheellinen hissin numero.")




talo = Talo(1, 10, 3)
talo.aja_hissiä(1, 5)
talo.aja_hissiä(2, 7)
talo.aja_hissiä(1, 1)
