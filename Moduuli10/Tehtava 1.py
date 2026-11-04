class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen = alin

    def hissi_ylös(self):
        if self.nykyinen < self.ylin:
            self.nykyinen += 1
            print(f"Hissi on kerroksessa {self.nykyinen}")

    def hissi_alas(self):
        if self.nykyinen > self.alin:
            self.nykyinen -= 1
            print("Hissi on kerroksessa", self.nykyinen)

    def mene_kerrokseen(self, kohde):
        while self.nykyinen < kohde:
            self.hissi_ylös()

        while self.nykyinen > kohde:
            self.hissi_alas()

h = Hissi(1, 10)
h.mene_kerrokseen(5)
h.mene_kerrokseen(1)
