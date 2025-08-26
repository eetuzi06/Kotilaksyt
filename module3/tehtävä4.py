vuosi = int(input("Anna vuosiluku: "))

if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
    print("Vuosiluku on karkausvuosi.")
else:
    print("Vuosiluku ei ole karkausvuosi.")