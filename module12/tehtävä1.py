import requests

dummy = input("Paina enter, jos haluat Chuck Norris vitsin")

pyyntö = "https://api.chucknorris.io/jokes/random"

vastaus = requests.get(pyyntö).json()
print(vastaus['value'])