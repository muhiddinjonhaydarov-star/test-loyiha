class Doira:
    def __init__(self, radius):
        self.radius = radius
    def yuza(self):
        return 3.14 * self.radius * self.radius
    def uzunlik(self):
        return 2 * 3.14 * self.radius
d = Doira(1000000)
print("Yuzasi:", d.yuza())
print("Uzunlig:", d.uzunlik())