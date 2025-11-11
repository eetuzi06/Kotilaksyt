from flask import Flask, jsonify

app = Flask(__name__)


def alkuluku(onko):
    if onko < 2:
        return False

    for i in range(2, int(onko ** 0.5) + 1):
        if onko % i == 0:
            return False
    return True


@app.route('/alkuluku/<onko>', methods=['GET'])
def onko_alkuluku(onko):
    try:
        luku = int(onko)
        tulos = alkuluku(luku)
        return jsonify({"Number": luku, "isPrime": tulos})
    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen merkki"
        }
        return jsonify(vastaus), tilakoodi


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)