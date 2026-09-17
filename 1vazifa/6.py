class Kino:
    def __init__(self, nomi, davomiyligi, reyting):
        self.nomi = nomi
        self.davomiyligi = davomiyligi
        self.reyting = reyting
    def malumot(self):
        soat = self.davomiyligi // 60
        daqiqa = self.davomiyligi % 60
        print(self.nomi, "-", soat, "soat", daqiqa, "daqiqa -", self.reyting, "ball")
k = Kino("Shaytanat", 169, 8.7)
k.malumot()