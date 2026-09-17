
import pyttsx3

def dvigatel_yarat():
    dvigatel = pyttsx3.init()
    dvigatel.setProperty('rate', 150)     
    dvigatel.setProperty('volume', 1.0)   
    return dvigatel


def ovozlarni_royxatla(dvigatel):
    ovozlar = dvigatel.getProperty('voices')
    print("=== Mavjud ovozlar ===")
    for i, v in enumerate(ovozlar):
        print(f"{i}: {v.name}")
    print()
    return ovozlar


def ovoz_tanla(dvigatel, kalit_soz):
   
    ovozlar = dvigatel.getProperty('voices')
    for v in ovozlar:
        if kalit_soz.lower() in v.name.lower() or kalit_soz.lower() in v.id.lower():
            dvigatel.setProperty('voice', v.id)
            print(f"✅ Tanlangan ovoz: {v.name}")
            return True
    print(f"⚠️ '{kalit_soz}' nomli ovoz topilmadi, standart ovoz ishlatiladi.")
    return False


def matnni_ayt(dvigatel, matn):
    dvigatel.say(matn)
    dvigatel.runAndWait()


def faylga_saqla(dvigatel, matn, fayl_nomi="chiqish.mp3"):
    dvigatel.save_to_file(matn, fayl_nomi)
    dvigatel.runAndWait()
    print(f"✅ '{fayl_nomi}' fayliga saqlandi!")


if __name__ == "__main__":
    dvigatel = dvigatel_yarat()

    ovozlarni_royxatla(dvigatel)

 
    ovoz_tanla(dvigatel, "Irina")     # Ruscha ovoz
    # ovoz_tanla(dvigatel, "David")       # Erkak, inglizcha ovoz
    # ovoz_tanla(dvigatel, "Zira")      # Ayol, inglizcha ovoz

    matn = "Ovozga aylantirmoqchi bo'lgan matningizni yozing: _."

   
    matnni_ayt(dvigatel, matn)

   
    faylga_saqla(dvigatel, matn, "chiqish.mp3")