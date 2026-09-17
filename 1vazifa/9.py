class Kutibxona:
    def __init__(self):
        self.kitob = {}

    def qoshish(self, nomi, soni=1):
        self.kitob[nomi] = self.kitob.get(nomi, 0) + soni

    def olish(self, nomi):
        if nomi not in self.kitob or self.kitob[nomi] == 0:
            print(f"'{nomi}' mavjud emas")
        else:
            self.kitob[nomi] -= 1

    def qaytarish(self, nomi):
        if nomi in self.kitob:
            self.kitob[nomi] += 1
kitob = Kutibxona()
kitob.qoshish("Kitob 1", 2)
kitob.olish("Kitob 1")
kitob.olish("Kitob 2")  
kitob.qaytarish("Kitob 1")