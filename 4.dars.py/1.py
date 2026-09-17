# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
# s1 = Person("Doniyorbek",19)
# print(s1.name,s1.age)





# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self,value):
        
#         if value < 0:
#             print("Xatolik: yosh manfiy bo'lishi mumkin emas")
#         else:
#             self.__age = value

# s1 = Person("Doniyorbek",19)

# print((s1.age))
# s1.age = -5
# s1.age = 21
# print(s1.name,s1.age)





# class Student(Person):
#     def __init__(self,name,age,grade):
#             super().__init__(name,age)
#             self.grade = grade
# class Teacher(Person):
#     def __init__(self,name,age,subject):
#         super().__init__(name,age)
#         self.subject = subject

# student1 = Student("Doniyorbek",19,"BOOTCAMP")
# teacher1 = Teacher("Otabek Tursunov",23,"Dasturlash")
# print(student1.name, student1.grade)
# print(teacher1.name,teacher1.subject)

# # .................................................................................

# class Student(Person):
#     def __init__(self,name,age,grade):
#             super().__init__(name,age)
#             self.grade = grade
#     def introduce(self):
#         return f"Salom, men {self.name}, {self.grade} - kurs o'qiman"
# class Teacher(Person):
#     def __init__(self,name,age,subject):
#         super().__init__(name,age)
#         self.subject = subject
#     def introduce(self):
#         return f"Salom, men {self.name}, {self.subject} fan dars beraman"
# people = [
#     Student("Doniyorbek",19, "BOOTCAMP"),
#     Teacher("Otabek Tursunov",23,"Dasturlash"),
# ]
# for person in people:
#     print(person.introduce())
# student1 = Student("Doniyorbek",19,"4 - oy")
# teacher1 = Teacher("Otabek Tursunov",23,"Dasturlash")
# print(student1.name, student1.grade)
# print(teacher1.name,teacher1.subject)




# from abc import ABC, abstractmethod
# class Person(ABC):
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self,value):
#         if value < 0:
#             print("Xatolik: yosh manifiy bo'lishi mumkin emas")
#         else:
#             self.__age  = value
#     @abstractmethod
#     def introduce(self):
#         pass



# class Person(ABC):
#     def __str__(self):
#         return f"{self.name} ({self.age}) yosh)"
#     def __eq__(self,other):
#         return self.name == other.name
# print(student1)
# print(student1 == teacher1)


# class Person(ABC):
#     @staticmethod
#     def average_age(people_list):
#         total = sum(p.age for p in people_list)
#         return round(total / len(people_list), 1)
# avg = Person.average_age([student1,teacher1])
# print(avg)

# class Classroom:
#     def __init__(self,room_name):
#         self.room_name = room_name
#         self.members = []
#     def add_member(self,person):
#         self.members.append(person)
#         print(f"'{person.name}'{self.room_name} kursga qo'shildi")
#     def show_all(self):
#         print(f"\n--- {self.room_name} tarkibi ---")
#         for person in self.members:
#             print(person)
#             print("  ",person.introduce())
# student1 = Student("Doniyorbek",19,"4 - oy")
# teacher1 = Teacher("Otabek Tursunov",23,"Dasturlash")


# Classroom = Classroom("4 -Oylik kursi")
# Classroom.add_member(student1)
# Classroom.add_member(teacher1)
# Classroom.show_all()
# print(f"\nO'rtacha yosh: {Person.average_age(Classroom.members)}")



class Kitob:
    def __init__(self, nomi, muallifi, mavjud=True):
        self.nomi = nomi
        self.muallifi = muallifi
        self.mavjud = mavjud

    def info(self):
        return f"{self.nomi} - {self.muallifi}"


class Kutubxona:
    def __init__(self):
        self.kitoblar = []

    def add_book(self,nomi,muallifi):
        yangi_kitob = Kitob(nomi,muallif)
        self.kitoblar.append(yangi_kitob)
        print(f"'{nomi}'kitobi kutubxonaga qo'shildi.")

    def show_books(self):
        if not self.kitoblar:
            print(Kutub )

k1 = Kitob("Sariq Devni Minib", "?")
k2 = Kitob("O'tkan kunlar", "Hoshimjon")

kutubxona = Kutubxona()
kutubxona.add_book(k1)
kutubxona.add_book(k2)

print("Kutubxona kitoblari:")
kutubxona.show_books()