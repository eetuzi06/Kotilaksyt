
pituus = int(input("Anna kuhan pituus (cm): "))

if pituus < 37:
    puutos = 37 - pituus
    print(f"Kuha on {puutos} cm pienempi alimmasta pyyntimitasta, laske kuha takaisin järveen.")
else:
    print("Kuha on yli alimman sallitun pyyntimitan, saat pitää sen.")
