class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @staticmethod
    def is_valid_salary(amount):
        return amount > 0
    @classmethod
    def from_string(cls, data):
        parts = data.split("-")
        name = parts[0].strip()
        salary = float(parts[1].strip())
        return cls(name, salary)
    def __str__(self):
        return f"Ism: {self.name}, Maosh: {self.salary}"
print(Employee.is_valid_salary(120000))   
print(Employee.is_valid_salary(-5000))   
emp1 = Employee.from_string("Doni -120000")
print(emp1)
emp2 = Employee.from_string("Ali -3500000")
print(emp2)