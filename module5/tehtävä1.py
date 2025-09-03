import random
summa = 0
maara = int(input("Anna arpakuutioiden lukumäärä: "))

for i in range(maara):
    kuutio = random.randint(1, 6)
    summa = summa + kuutio
print(f"Tulostettujen lukujen summa: {summa}")


