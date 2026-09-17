class Temperature:
    def __init__(self, harorat):
        self.harorat = harorat

    def __str__(self):
        return f"{self.harorat}°C"

    def __eq__(self, other):
        return self.harorat == other.harorat

    def __lt__(self, other):
        return self.harorat < other.harorat

t1 = Temperature(25)
t2 = Temperature(25)
t3 = Temperature(30)

print(t1)
print(t1 == t2)
print(t1 < t3)
print(t3 < t1)