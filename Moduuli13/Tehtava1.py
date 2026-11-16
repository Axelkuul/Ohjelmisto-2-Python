from flask import Flask

app = Flask(__name__)

def onko_alukuluku(luku):
    if luku <= 1:
        return False

    for i in range (2, luku):
        if luku % i == 0:
            return False

    return True

@app.route("/alkuluku/<int:luku>")
def tarkista_alkuluku(luku):
    tulos = onko_alukuluku(luku)
    vastaus = {
        "Numero": luku,
        "Onko alkuluku?": tulos,
    }
    return (vastaus)

if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)