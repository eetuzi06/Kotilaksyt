
jaettavat = 0
kys = int(input("Anna kokonaisluku: "))

for i in range(2, kys):
    if kys % i == 0:
        jaettavat = jaettavat + 1

if jaettavat == 0:
    print(f"Luku {kys} on alkuluku.")

else:
    print(f"Luku {kys} ei ole alkuluku.")





