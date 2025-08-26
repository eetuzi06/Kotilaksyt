sukupuoli = input("Kerro biologinen sukupuolesi: ")
gl = int(input("Anna hemoglobiiniarvosi (g/l): "))

if sukupuoli == "mies":
    if gl < 134:
        print("Hemoglobiiniarvosi ovat alhaiset.")
    elif gl <= 175:
        print("Hemoglobiiniarvosi ovat normaalit.")
    elif gl > 175:
        print("Hemoglobiiniarvosi ovat korkeat.")

elif sukupuoli == "nainen":
    if gl < 117:
        print("Hemoglobiiniarvosi ovat alhaiset.")
    elif gl <= 195:
        print("Hemoglobiiniarvosi ovat normaalit.")
    elif gl > 195:
        print("Hemoglobiiniarvosi ovat korkeat.")



