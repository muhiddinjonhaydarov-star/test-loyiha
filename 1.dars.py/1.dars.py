# class Student:
#     def  __init__(self,ism,yosh,yonalishi):
#         self.ism = ism
#         self.yosh = yosh
#         self.yonalishi = yonalishi
# s1 = Student("Jasur",14,"SMM")
# s2 = Student("Doniyorbek",19,"Kiberxavsizlik")

# print(f"Talabalar" : {s1.ism},{s1.yosh},{s1.yonalishi})
# print(f"Talabalar" : {s2.ism},{s2.yosh},{s2.yonalishi})

import datetime


class Hisob:
    def __init__(self, ism, fam, karta_raqami, balans=0):
        self.ism = ism
        self.fam = fam
        self.karta_raqami = karta_raqami
        self.balans = balans
        self.kirimlar = []
        self.chiqimlar = []

    def malumot(self):
        return f"Ega: {self.ism} {self.fam}\nKarta: {self.karta_raqami}"

    def balansni_korish(self):
        return f"Balans: ${self.balans}"

    def kirimlar_tarixi(self):
        template = "------------------\nKirimlar:\n"
        for i, kirim in enumerate(self.kirimlar, start=1):
            template += f"{i}. {kirim.get('vaqt')} -- ${kirim.get('miqdor')} -- {kirim.get('izoh')}\n"
        return template

    def chiqimlar_tarixi(self):
        template = "------------------\nChiqimlar:\n"
        for i, chiqim in enumerate(self.chiqimlar, start=1):
            template += f"{i}. {chiqim.get('vaqt')} -- ${chiqim.get('miqdor')} -- {chiqim.get('izoh')}\n"
        return template

    def kirim(self, miqdor, izoh=""):
        self.balans += miqdor
        self.kirimlar.append({
            "miqdor": miqdor,
            "izoh": izoh,
            "vaqt": datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        })

    def chiqim(self, miqdor, izoh=""):
        assert miqdor <= self.balans, "Balansda mablag' yetarli emas!"
        self.balans -= miqdor
        self.chiqimlar.append({
            "miqdor": miqdor,
            "izoh": izoh,
            "vaqt": datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        })


class Task:
    def __init__(self, text, status='yangi'):
        self.text = text
        self.status = status


class Todo:
    def __init__(self, owner):
        self.owner = owner
        self.tasks = []

    def add_task(self, new_task: Task):
        self.tasks.append(new_task)

    def get_tasks(self):
        result = ""
        for id, task in enumerate(self.tasks, start=1):
            belgi = '🚫' if task.status == 'yangi' else '🟢'
            result += f"\n[ID: {id}] {task.text} -- {belgi}"
        return result

    def delete_task(self, id):
        self.tasks.pop(id - 1)
        print("Muvaffaqiyatli o'chirildi!")

    def status_mark(self, id, new_status='completed'):
        self.tasks[id - 1].status = new_status


doniyorbek = Todo("Doniyorbek")

while True:
    buyruqlar = int(input(
        "\n1 -> Rejalar\n2 -> Reja qo'shish\n3 -> Rejani o'chirish\n"
        "4 -> Statusni o'zgartirish\n0 -> Chiqish.\n\nBuyruq kiriting: "
    ))

    match buyruqlar:
        case 0:
            print("Xayr!")
            break
        case 1:
            if doniyorbek.tasks:
                print(doniyorbek.get_tasks())
            else:
                print("\nRejalar mavjud emas!")
        case 2:
            text = input("Yangi reja: ")
            doniyorbek.add_task(Task(text))
            print("\nReja muvaffaqiyatli qo'shildi!")
        case 3:
            print(doniyorbek.get_tasks())
            id = int(input("\nO'chirish uchun ID kiriting: "))
            doniyorbek.delete_task(id)
        case 4:
            print(doniyorbek.get_tasks())
            id = int(input("\nStatus o'zgartirish uchun ID kiriting: "))
            doniyorbek.status_mark(id)
            print("Status yangilandi!")
        case _:
            print("Noto'g'ri buyruq!")