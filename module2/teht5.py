leiviska = float(input("Anna leivisköjen määrä: "))
naula = float(input("Anna naulojen määrä: "))
luoti = float(input("Anna luodit: "))

grammoja_per_leiviska = 20
grammoja_per_naula = 32
grammoja_per_luoti = 13.3

grammat = (leiviska * grammoja_per_leiviska * grammoja_per_naula * grammoja_per_luoti) + \
          (naula * grammoja_per_naula * grammoja_per_luoti) + \
          (luoti * grammoja_per_luoti)

kilot = grammat // 1000
loppugrammat = grammat % 1000

print(f"Massa nykymittojen mukaan: {kilot:.0f} kg ja {loppugrammat:.2f} g")