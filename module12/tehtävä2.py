import requests

api_key = "3cd6b07a72edc1c1a5b7134d938b31ad"

kaupunki = input("Anna kaupungin nimi: ")

pyynto = f"https://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={api_key}&units=metric&lang=fi"

vastaus = requests.get(pyynto)
if vastaus.status_code == 200:
    weather = vastaus.json()
    lampotila = weather["main"]["temp"]
    säätila = weather["weather"][0]["description"]
    print (f"Sää kaupungissasi {kaupunki}: {säätila}, {lampotila:.1f} °C")