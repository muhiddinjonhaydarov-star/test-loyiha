class Savat:
    def __init__(self):
        self.mahsulotlar = []
    def qoshish(self, mahsulot):
        self.mahsulotlar.append(mahsulot)
    def ochirish(self, mahsulot):
        if mahsulot in self.mahsulotlar:
            self.mahsulotlar.remove(mahsulot)
    def korsatish(self):
        for m in self.mahsulotlar:
            print(m)
savat = Savat()
savat.qoshish("Non")
savat.qoshish("Sut")
savat.qoshish("Tuxum")

savat.korsatish()

savat.ochirish("Sut")
print("---")
savat.korsatish()