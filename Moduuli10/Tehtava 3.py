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
            print(f"Hissi on kerroksessa {self.nykyinen}")

    def mene_kerrokseen(self, kohde):
        while self.nykyinen < kohde:
            self.hissi_ylös()

        while self.nykyinen > kohde:
            self.hissi_alas()


class Talo:
    def __init__(self, alin, ylin, hissien_lukumaara):
        self.hissit = []

        for i in range(hissien_lukumaara):
            hissi = Hissi(alin, ylin)
            self.hissit.append(hissi)

    def aja_hissiä(self, hissin_numero, kohdekerros):
        self.hissit[hissin_numero - 1].mene_kerrokseen(kohdekerros)

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.mene_kerrokseen(1)


talo = Talo(1, 10, 3)

talo.aja_hissiä(1, 5)
talo.aja_hissiä(2, 8)
talo.aja_hissiä(3, 3)

print("Palohälytys!")
talo.palohälytys()
