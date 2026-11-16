from flask import Flask
import mysql.connector

app = Flask(__name__)

def hae_lentokentta(icao):
    yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='Alexander',
         password='Lokki123',
         autocommit=True
         )

    kursori = yhteys.cursor()
    sql = "SELECT ident, name, municipality FROM airport WHERE ident = %s"
    kursori.execute(sql, (icao,))
    tulos = kursori.fetchone()
    
    kursori.close()
    yhteys.close()
    return tulos

@app.route("/kenttä/<icao>")
def kentta_teidot(icao):
    tulos = hae_lentokentta(icao)

    if tulos:
        vastaus = {
            "ICAO-koodi ": tulos[0],
            "Nimi ": tulos[1],
            "Paikkakunta ": tulos[2]
        }
        return (vastaus)
    else:   
        return("Lentokenttää ei löytynyt.")

if __name__ == "__main__":
    app.run(use_reloader=True, host= "127.0.0.1", port =3000)
    