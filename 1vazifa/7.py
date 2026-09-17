class Harorat:
    def __init__(self, selsiy):
        self.selsiy = selsiy

    def fahrengeytga(self):
        return self.selsiy * 9 / 5 + 32

    def kelvinga(self):
        return self.selsiy + 273.15
h = Harorat(25)
print("Selsiy:", h.selsiy)
print("Farengeyt:", h.fahrengeytga())
print("Kelvin:", h.kelvinga())