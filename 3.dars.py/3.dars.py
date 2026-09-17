# class Book:
#     def __init__(self,nomi,muqova):
#         self.nomi = nomi
#         self.muqova = muqova
#     def __str__(self):
#         return f"[{self.nomi}]{self.muqova}"
# s1 = Book("SOS","100")
# print(s1)


# class Butun:
#     def __init__(self, son):
#         self.son = son

#     def __str__(self):
#         return str(self.son)

#     def __add__(self, other):
#         return self.son + other.son

#     def __sub__(self, other):
#         return self.son - other.son

#     def __mul__(self, other):
#         return self.son * other.son

#     def __eq__(self, value):
#         return self.son == value.son

#     def __gt__(self, other):
#         return self.son > other.son


# son1 = Butun(10)
# son2 = Butun(15)
# print(son1 + son2)
# print(son2 - son1)

# print(son1 == son2)
# print(son1 > son2)
# print(10 == 15)



# from abc import ABC, abstractmethod


# class Shakl(ABC):
#     @abstractmethod
#     def yuza(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass


# class Tortburchak(Shakl):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def yuza(self):
#         return self.a * self.b

#     def perimeter(self):
#         return 2 * (self.a + self.b)


# t = Tortburchak(4, 11)
# print(t.yuza())
# print(t.perimeter())

# ..................................................................
# class BankCard:
#     def __init__(self, ega, karta_raqam):
#         self.ega = ega
#         self.karta_raqam = karta_raqam

#     def info(self):
#         return f"{self.ega}:{self.karta_raqam}"

#     @staticmethod
#     def bank_info():
#         return "Najot bank MCHJ"


# b1 = BankCard("Doniyorbek Muhiddinov", "8600 1234 5678 9876")
# print(b1.info())
# print(b1.bank_info())
# print(BankCard.bank_info())
# ......................................................................

# class Matematika:
#     @staticmethod
#     def daraja(a:float,b:float) -> float:
#         return a ** b
#     @staticmethod
#     def factorial(a: int) -> int:
#         f = 1
#         for i in range(2, a + 1):
#             f *= i
#         return f
#     @staticmethod
#     def past_yaxlit(a):
#         return int(a)
#     @staticmethod
#     def yuqori_yaxlit(a):
#         return int(a) + 1
# print(Matematika.factorial(5))
# print(Matematika.past_yaxlit(14.99))
# print(Matematika.yuqori_yaxlit(14.99))


# class Student:
#     school_name = "Python Academy"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_birth_year(cls, name, birth_year):
#         age = 2026 - birth_year
#         return cls(name, age)

#     @classmethod
#     def change_school(cls, new_name):
#         cls.school_name = new_name


# student1 = Student.from_birth_year("Aziz", 2007)
# print(student1.age)
# Student.change_school("Farg'ona IT school")
# print(Student.school_name)


class Cart:
    @staticmethod
    def mahsulot(nomi,narxi,soliq):
        return narxi - narxi * (soliq/100)
    def  __len__(self):
        return len(self.narxi)
    def __str__(self):
        return f"Korzina: {len(self.)}"
    @staticmethod
    def mahsulot(nomi,narxi,soliq):
        return narxi - narxi * (soliq / 100)
daromad = Cart.mahsulot(500,10)
print(daromad)