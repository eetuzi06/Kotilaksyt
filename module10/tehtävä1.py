class Hissi:
    def __init__(self, ylinkerros, alinkerros):
        self.ylinkerros = ylinkerros
        self.alinkerros = alinkerros
        self.nyky = alinkerros

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

h = Hissi(alinkerros=1, ylinkerros=10)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)


