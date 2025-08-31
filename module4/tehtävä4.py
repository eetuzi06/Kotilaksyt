import random
luku = int(random.randint(1, 10))
arvaa = 0

while arvaa != luku:
    arvaa = int(input("Arvaa luku väliltä 1-10: "))

    if arvaa < luku:
        print("Liian pieni arvaus")
    elif arvaa > luku:
        print("Liian suuri arvaus")
else:
    print("Oikein!")




