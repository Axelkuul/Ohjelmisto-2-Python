class Inventaario:
    lista = []
    def _init_(self, tavara=[]):
        self.tavara = tavara
    def _init_(self, tavara):
        self.lista.append(self, tavara)
    
    def tulosta_tavarat(self):
        for tavara in self.tavara:
            print(tavara)


pelaajan_tavara = Inventaario(["miekka", "kilpi"])
pelaajan_tavara.tulosta()
pelaajan_tavara.tulosta