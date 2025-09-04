import math
def pizza(halkaisija, eurot):
    halkm = halkaisija / 100
    sade = halkm / 2
    pintaala = math.pi * sade ** 2
    return eurot / pintaala
halk1 = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta (€): "))
halk2 = float(input("Anna toisen pizzan halkaisija (cm): "))
hinta2 = float(input("Anna toisen pizzan hinta (€): "))

raha1 = pizza(halk1, hinta1)
raha2 = pizza(halk2, hinta2)

print(f"Ensimmäisen pizzan hinta per neliömetri: {raha1:.2f} €")
print(f"Toisen pizzan hinta per neliömetri: {raha2:.2f} €")

if raha1 > raha2:
    print("Ensimmäinen pizza antaa paremman rahan vastineen")
elif raha1 < raha2:
    print("Toinen pizza antaa paremman rahan vastineen")




