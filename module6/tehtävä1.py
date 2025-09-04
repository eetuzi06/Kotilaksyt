import random
noppa = 0

def heita ():
    return random.randint(1, 6)


while noppa != 6:
    noppa = heita()
    print(f"Nopan silmäluku: {noppa}")

