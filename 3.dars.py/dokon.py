# class savatcha:
#     def __init__(self):
#         self.maxsulotlar = []

#     def maxsulot_qosh(self, maxsulot):
#         self.maxsulotlar.append(maxsulot)

#     def maxsulotlarni_korish(self):
#         return self.maxsulotlar
#     def maxsulot_olish(self, maxsulot):
#         if maxsulot in self.maxsulotlar:
#             self.maxsulotlar.remove(maxsulot)
#         else:
#             return "Bunday maxsulot mavjud emas!"
#     def maxsulot_ochirish(self, maxsulot):
#         if maxsulot in self.maxsulotlar:
#             self.maxsulotlar.remove(maxsulot)
#         else:
#             return "Bunday maxsulot mavjud emas!"

# p = savatcha()


# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def show_info(self):
#         print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, name):
        self.items.append(name)
        print(f"'{name}' savatga qo'shildi")

    def remove_item(self, name):
        if name in self.items:
            self.items.remove(name)
            print(f"'{name}' savatdan o'chirildi")
        else:
            print(f"'{name}' savatda topilmadi")

    def show_items(self):
        if not self.items:
            print("Savat bo'sh")
        else:
            print("Savatdagi mahsulotlar:", ", ".join(self.items))


cart1 = Cart()
cart1.add_item("Non")
cart1.add_item("Sut")
cart1.show_items()      # Savatdagi mahsulotlar: Non, Sut
cart1.remove_item("Non")
cart1.show_items()      # Savatdagi mahsulotlar: Sut
