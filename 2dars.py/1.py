# class Bankaccount:
#     def __init__ (self,karta,parol,balance):
#         self.karta = karta
#         self.__parol = parol
#         self.__balance = balance


#     def set_parol(self):
#         self.__parol = new_parol

#     def get_balance(self):
#         print(f"My balance: ${self.__balance}")
    
# s1 = Bankaccount("8600 0000 1111 2222","1234",10050)
# # print(s1.karta)
# # print(s1.parol)
# # print(s1.balance)
# s1.get_parol()


# class User:
#     def __init__(self,username,password,first_name,last_name):
#         self.username = username
#         self.__password = paswword
#         self.first_name = first_name
#         self.last_name = last_name
#     def info(self):
#         return f"Username:{self.username}\nFull Name:{self.first_name} {self.last_name}"
# doniyorbek = User('otabek','1234','Doniyorbek','Muhiddinov')
# print(doniyorbek.info())

# class Ustoz(User):
#     def __init__(self,username,password,first_name,last_name,salary,phone_number):
#         super().__init__(username,password,first_name,last_name)
#         self.salary = salary
#         self.phone_number = phone_nember

#     def get_password(self):
#         return self.password
#     def info(self):
#         return f"Foydalanuvchi nomi: {self.username}\nUstoz: {self.first_name} {self.last_name}"
# Ali = Ustoz('Ali','1234','Ali','Madaminov',1200,"+998 04 758 24 07")
# print(Ali.info())
# print(Ali.get_password)



# class Uzbekiston:
#     def __init__ (self,name,population,area):
#         self.name = name
#         self.population = population
#         self.area = area
#     def info(self):
#         return f"Uzbekistonning {self.name} shahrida {self.population} aholi yashaydi {self.area} ming km²"
# toshkent = Uzbekiston("Toshkent", 127653, 34.0)
# print(toshkent.info())
# class Rossiya(Uzbekiston):
#     def info(self):
#         return f"Rossiyaning{self.name}shaharda {self.poplation} aholi yashaydi. Maydoni {self.area} ming km²"

# moskow = Rossiya('Moskow',343454,123,3)
# print(moskow.info)()

