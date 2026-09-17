
from datetime import datetime

class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if value < 0:
            pass
        else:
            self.__age = value
    def __it__(self,other):
        return self.age < other.age
    def __repr__(self):
        return f"{self.name} ({self.age} yosh)"
    @classmethod
    def from_birth_year(cls,name,birth_year):
        hozrgi_yil = 2026
        age = hozrgi_yil - birth_year
        return cls(name,age)
p1 = Person.from_birth_year("Doniyorbek",2007)
print(p1)