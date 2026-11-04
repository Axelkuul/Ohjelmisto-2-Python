class Lentokone:
    def __init__(self, nimi, bensatankin_max, bensatankin_nyky):
        self.nimi = nimi
        self.bensatankin_max = bensatankin_max
        self.bensatankin_nyky = bensatankin_nyky

    def tulosta_tiedot(self):
        print(f"Kone{self.nimi}")
        print(f"Bensan maksimi määrä: {self.bensatankin_max}l")
        print(f"Bensan nykyinen määrä: {self.bensatankin_nyky}l")

Boeing737 = Lentokone("Boeing737", 10000, 4500) 

class Lentokentta:
    def __init__(self, nimi,):
        self.nimi = nimi
        self.koneet = []

    def lisaa_kone(self, kone):
        self.koneet.append(kone)

    def tulosta_kaikki(self):
        print(f"Kentällä {self.nimi} on nyt")
        for kone in self.koneet:
            kone.tulosta_tiedot()
            print("---")

    def tankkaa(self, kone):
        kone.bensatankin_nyky = kone.bensatankin_max
        print (f"Kone {kone.nimi} tankattu")

helsinki = Lentokentta("Helsink-Vantaa")
helsinki.lisaa_kone(Boeing737)
helsinki.tankkaa(Boeing737)
print("tankkauksen jälkeen")
Boeing737.tulosta_tiedot()
#keskeneräinen