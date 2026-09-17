class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    @property
    def grade(self):
        return self.__grade
    @grade.setter
    def grade(self, value):
        if value < 0 or value > 100:
            print("Xato: baholar 0 dan 100 gacha")
        else:
            self.__grade = value
    def introduce(self):
        return f"Men {self.name}, bahoyim: {self.grade}"
s1 = Student("Doniyorbek",19,89)
print(s1.introduce())
s1.grade = 120
s1.grade = 95
print(s1.grade)