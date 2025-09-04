gallona = 3.785
litrat = float(input("Anna bensiinin määrä nestegallonoina: "))

def bensa(gallona):
    litra = litrat * gallona
    return litra
bensa(gallona)
print(f"Bensiinin määrä litroissa {bensa(gallona)} litraa")

