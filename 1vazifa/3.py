class Telfon:
    def __init__(self, brend, batareya=100):
        self.brend = brend
        self.batareya = batareya
    def batareyani_kamaytir(self, foiz):
        self.batareya -= foiz
        if self.batareya < 0:
            self.batareya = 0
    def batareyani_oshir(self, foiz):
        self.batareya += foiz
        if self.batareya > 100:
            self.batareya = 100
tel = Telfon("Iphone", 80)
print(f"{tel.brend} batareyasi: {tel.batareya}%")
tel.batareyani_kamaytir(30)
print(f"Kamaytirilgandan keyin: {tel.batareya}%")
tel.batareyani_oshir(70)
print(f"Oshirilgandan keyin: {tel.batareya}%")