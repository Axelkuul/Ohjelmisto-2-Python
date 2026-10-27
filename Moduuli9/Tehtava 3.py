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

    def kulje(self, tuntia):
        self.matka += tuntia * self.nopeus

mersu = Auto("ABC-123", 142)
mersu.kiihdyta(60)
mersu.kulje(1.5)

print(f"Auton rekkari on {mersu.rekkari}")
print(f"Auton huippunopeus on {mersu.huippunopeus}km/h")
print(f"Auton tämänhetkinen nopeus on {mersu.nopeus}km/h")
print(f"Auton kuljettu matka on {mersu.matka}km")

