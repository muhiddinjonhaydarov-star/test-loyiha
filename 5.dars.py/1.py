# import requests
# response = requests.get('http://iamawesome.com')

# print(response)
# print(response.status_code)
# print(response.text)

# import wikipedia
# wikipedia.set_lang('uz')
# text = input("Nima qidirmoqchisiz: ")
# result = wikipedia.search(text)
# for title in result:
#     print(wikipedia.summary(title), end="\n\n")


# import asyncio
# from googletrans import Translator

# async def main(text):
#     translator = Translator()
#     natija = await translator.translate(text, src='uz', dest='ru')
#     print(natija.text)   

# asyncio.run(main(input(">>> ")))



# import requests
# from pprint import pprint
# data = requests.get("http://cbu.uz/uz/arkhiv-kursov-valyut/json/")
# pprint(data.json())
# data = data.json()
# tanlov = int(input("==VALYUTA KONVERTOR==\n1.USD=>\nUZS\n2.RUB=>UZS\n"))
# match tanlov:
#     case 1:
#         summa = float(input("Dollar miqdori kiriting:"))
#         for kurs in data:
#             if kurs["Ccy"] == "USD":
#                 print(f"{summa} USD = {summa*float(kurs["Rate"])}SO'M")
#                 break
#     case 2:
#         summa = float(input("Dollar miqdori kiriting:"))
#         for kurs in data:
#             if kurs["Ccy"] == "RUB":
#                 print(f"{summa} RUB = {summa*float(kurs["Rate"])}SO'M")
#                 break