import mariadb

yhteys = mariadb.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="eetul",
    passwd="0000",
    autocommit=True
)

valinta = input("Anna maakoodi: ")

def maakoodi(maa):
    sql = f"SELECT type, Count(*) FROM airport where iso_country = '{valinta}' GROUP BY type"
    cursor = yhteys.cursor()
    cursor.execute(sql, (maa,))
    tulos = cursor.fetchall()

    for koko, maara in tulos:
        print(f"{koko}: {maara} kpl")

maakoodi(valinta)

