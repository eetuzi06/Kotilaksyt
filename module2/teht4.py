import math
luku1 = int(input("Anna ensimmäinen kokonaisluku: "))
luku2 = int(input("Anna toinen kokonaisluku: "))
luku3 = int(input("Anna kolmas kokonaisluku: "))

summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = (luku1 + luku2 + luku3) / 3

print("Kokonaislukujen summa on: " + str(summa))
print("Kokonaislukujen tulo on: " + str(tulo))
print("Kokonaislukujen keskiarvo on: " + str(keskiarvo))