class Qoshiqlar:
    def __init__(self, nomi):
        self.nomi = nomi
        self.qoshiq = []

    def qoshish(self, qoshiq):
        self.qoshiq.append(qoshiq)

    def ochirish(self, qoshiq):
        self.qoshiq.remove(qoshiq)

    def soni(self):
        return len(self.qoshiq)

p = Qoshiqlar("Sevimlilar")
p.qoshish("Qo'shiq 1")
p.qoshish("Qo'shiq 2")
p.ochirish("Qo'shiq 1")
print(p.soni())  