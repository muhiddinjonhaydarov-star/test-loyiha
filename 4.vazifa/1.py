class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
s1 = Person("Doniyorbek",19)
print(s1.name,s1.age)





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
            print("Xatolik: yosh manfiy bo'lishi mumkin emas")
        else:
            self.__age = value

s1 = Person("Doniyorbek",19)

print((s1.age))
s1.age = -5
s1.age = 21
print(s1.name,s1.age)




class Student(Person):
    def __init__(self,name,age,grade):
            super().__init__(name,age)
            self.grade = grade
class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject = subject

student1 = Student("Doniyorbek",19,"BOOTCAMP")
teacher1 = Teacher("Otabek Tursunov",23,"Dasturlash")
print(student1.name, student1.grade)
print(teacher1.name,teacher1.subject)


class Student(Person):
    def __init__(self,name,age,grade):
            super().__init__(name,age)
            self.grade = grade
    def introduce(self):
        return f"Salom, men {self.name}, {self.grade} - kurs o'qiman"
class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject = subject
    def introduce(self):
        return f"Salom, men {self.name}, {self.subject} fan dars beraman"
people = [
    Student("Doniyorbek",19, "BOOTCAMP"),
    Teacher("Otabek Tursunov",23,"Dasturlash"),
]
for person in people:
    print(person.introduce())
student1 = Student("Doniyorbek",19,"4 - oy")
teacher1 = Teacher("Otabek Tursunov",23,"Dasturlash")
print(student1.name, student1.grade)
print(teacher1.name,teacher1.subject)

class Principal(Person):
    def __init__(self,name,age,years_of_experiece):
        super().__init__(name,age)
        self.years_of_experiece = years_of_experiece
        print(f"Maktab direktori va {self.years_of_experiece} yilik tajriba")

    def introduce(self):
        return f"Salom, men {self.name}, maktab direktoriman, {self.years_of_experiece} yillik tajribaga egaman"

student1 = Student("Doniyorbek",19,4)
principal = Principal("A.Holmatov",45,22)

print(student1.introduce())
print(teacher1.introduce())
print(principal.introduce())