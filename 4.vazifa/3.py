class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def __it__(self,other):
        return self.age < other.age
    def __repr__(self):
        return f"{self.name} ({self.age} yosh)"

class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade
    
    def introduce(self):
        return f"Men {self.name}, Bahoyim {self.grade}"
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __repr__(self):
        return f"{self.name} ({self.age} yosh)"


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def introduce(self):
        return f"Salom, men {self.name}, bahoyim {self.grade}"


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        return f"Salom, men {self.name}, {self.subject} fan dars beraman"


class Classroom:
    def __init__(self):
        self.members = []

    def add_member(self, person):
        self.members.append(person)


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
        return f"{self.name} ({self.age} yosh)"

class Classroom:
    def __init__(self):
        self.members = []

    def add_member(self,person):
        self.members.append(person)
classroom = Classroom()
classroom.add_member(Student("Doniyorbek",19,95))
classroom.add_member(Teacher("Otabek Tursunov",23,"Dasturlash"))
classroom.add_member(Student("Madina Yusupva",20,99))
for person in sorted(classroom.members):
    print(person)
