class Vehicle:
    def start_engine(self):
        return "Dvigatel ishga tushdi"
    def stop_engine(self):
        return "Dvigatel o'chdi"
class Car(Vehicle):
    pass
class Motorcycle(Vehicle):
    pass
car = Car()
motorcycle = Motorcycle()
print(car.start_engine())
print(car.stop_engine())
print(motorcycle.start_engine())
print(motorcycle.stop_engine())