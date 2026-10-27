class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0


mersu = Auto("ABC-123", 142)

print(f"Auton rekkari on {mersu.rekkari}")
print(f"Auton huippunopeus on {mersu.huippunopeus}km/h")
print(f"Auton tämänhetkinen nopeus on {mersu.nopeus}km/h")
print(f"Auton kuljettu matka on {mersu.matka}km")
        