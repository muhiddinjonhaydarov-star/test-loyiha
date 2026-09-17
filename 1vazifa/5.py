class Xodim:
    def __init__(self, ism, maosh):
        self.ism = ism
        self.maosh = maosh
    def maoshni_oshir(self, summa):
        self.maosh += summa
        print(f"{self.ism}ning yangii maoshi: {self.maosh}")
x = Xodim("Doni", 3000000)
x.maoshni_oshir(500000)