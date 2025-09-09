kuukaudet = ("Talvi", "Talvi", "Kevät", "Kevät", "Kevät", "Kesä", "Kesä", "Kesä", "Syksy", "Syksy", "Syksy", "Talvi")

anna = int(input("Anna kuukauden numero (1-12): "))

kuukausi = kuukaudet[anna-1]
print (f"{anna}. kuukausi on {kuukausi}.")


