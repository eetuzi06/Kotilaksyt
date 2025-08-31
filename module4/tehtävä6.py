import random

N = int(input("Arvottavien pisteiden määrä: "))

lasku = 0
osuma = 0

while lasku < N:

    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    if x ** 2 + y ** 2 < 1:
        osuma = osuma + 1

    lasku = lasku + 1

likiarvo = 4 * osuma / N
print(f"Piin likiarvo: {likiarvo}")






