import random
noppa = 0

def heita (tahkot):
    silma =  random.randint(1, tahkot)
    return silma

tahkot = int(input("Anna tahkojen määrä: "))
while noppa != tahkot:
    noppa = heita(tahkot)
    print(f"Nopan silmäluku: {noppa}")