class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        self.nopeus = self.nopeus + muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

mersu = Auto("ABC-123", 142)

mersu.kiihdyta(30)
mersu.kiihdyta(70)
mersu.kiihdyta(50)
print(f"Auton nopeus on {mersu.nopeus}")
mersu.kiihdyta(-200)
print(f"Auton nopeus äkkijarrutuksen jälkeen on {mersu.nopeus}")

print(f"Auton rekkari on {mersu.rekkari}")
print(f"Auton huippunopeus on {mersu.huippunopeus}km/h")
print(f"Auton tämänhetkinen nopeus on {mersu.nopeus}km/h")
print(f"Auton kuljettu matka on {mersu.matka}km")