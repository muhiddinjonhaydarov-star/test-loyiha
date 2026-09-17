from datetime import datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            print("Xatolik: yosh manfiy bo'lishi mumkin emas")
        else:
            self.__age = value

    def __lt__(self, other):
        return self.age < other.age

    def __repr__(self):
        return f"{self.name} ({self.age} yosh)"

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = datetime.now().year   
        age = current_year - birth_year        
        return cls(name, age)                  


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
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
        return f"Salom, men {self.name}, bahoyim {self.grade}"


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        return f"Salom, men {self.name}, {self.subject} fan dars beraman"


class Principal(Person):
    def __init__(self, name, age, years_of_experiece):
        super().__init__(name, age)
        self.years_of_experiece = years_of_experiece
        print(f"Maktab direktori va {self.years_of_experiece} yilik tajriba")

    def introduce(self):
        return f"Salom, men {self.name}, maktab direktoriman, {self.years_of_experiece} yillik tajribaga egaman"


class Classroom:
    def __init__(self):
        self.members = []

    def add_member(self, person):
        self.members.append(person)

    def count_students(self):
        count = 0
        for member in self.members:
            if isinstance(member, Student):
                count += 1
        return count

    def count_teachers(self):
        count = 0
        for member in self.members:
            if isinstance(member, Teacher):
                count += 1
        return count

    def find_by_name(self, name):
        for member in self.members:
            if member.name == name:
                return member
            pass


# ----------------- Sinash (test) qismi -----------------
if __name__ == "__main__":
    classroom = Classroom()

    classroom.add_member(Student("Doniyorbek", 19, 95))
    classroom.add_member(Teacher("Otabek Tursunov", 23, "Dasturlash"))
    classroom.add_member(Student("Madina Yusupova", 20, 88))
    classroom.add_member(Principal("A.Holmatov", 45, 22))

    print("\n--- Barcha a'zolar (yosh bo'yicha saralangan) ---")
    for person in sorted(classroom.members):
        print(person)

    print("\n--- Tanishtiruv (introduce) ---")
    for person in classroom.members:
        print(person.introduce())

    print("\n--- Hisoblar ---")
    print("O'quvchilar soni:", classroom.count_students())
    print("O'qituvchilar soni:", classroom.count_teachers())

    print("\n--- Ism bo'yicha qidirish ---")
    print(classroom.find_by_name("Madina Yusupova"))
    print(classroom.find_by_name("Nomavjud"))

    print("\n--- from_birth_year ---")
    person1 = Person.from_birth_year("Sardor", 2005)
    print(person1)