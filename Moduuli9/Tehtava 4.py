import random
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



autot = []
for i in range(1,11): 
    rekkari = f"ABC{i}"
    huippunopeus = random.randint(100, 200)

    auto = Auto(rekkari, huippunopeus)
    autot.append(auto)


while not any(auto.matka >= 10000 for auto in autot):
    for auto in autot:
        auto.kiihdyta(random.randint(-10, 15))
        auto.kulje(1)
  
print(f"{'Rekisteri':<12} {'Huippunopeus':<16} {'Nopeus':<10} {'Matka':<10}")

for auto in autot:
    print(f"{auto.rekkari:<12} {auto.huippunopeus:<16} "
          f"{auto.nopeus:<10} {auto.matka:<10.1f}")