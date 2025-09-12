import mariadb

yhteys = mariadb.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="eetul",
    passwd="0000",
    autocommit=True
)

valinta = input("Anna lentokentän ICAO-koodi: ")


def lentokentta():
    sql = f"SELECT name, continent from airport where ident like '{valinta}'"
    kursori = yhteys.cursor()
    kursori.execute(sql, (valinta,))
    tulokset = kursori.fetchall()

    for nimi, kunta in tulokset:
        print(nimi, kunta)


lentokentta()