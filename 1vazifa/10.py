class Quiz:
    def __init__(self, ism, savollar):
        self.ism = ism
        self.savollar = savollar
        self.javoblar = 0

    def j_belgilash(self, togri=True):
        if togri:
            self.javoblar += 1

    def foiz(self):
        return round(self.javoblar / self.savollar * 100)

    def natija(self):
        return f"{self.ism}: {self.javoblar}/{self.savollar} ({self.foiz()}%)"
q = Quiz("Aziz", 10)
q.j_belgilash(True)
q.j_belgilash(True)
q.j_belgilash(False)

print(q.natija()) 