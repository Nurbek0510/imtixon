import json

with open("imtixon3/olma/products.json", "r") as fayl:
    mahsulotlar = json.load(fayl)

nom = input("Mahsulot nomi: ")
yangi_miqdor = int(input("Yangi miqdor: "))

topildi = False

for mahsulot in mahsulotlar:
    if mahsulot["nom"].lower() == nom.lower():
        mahsulot["miqdor"] = yangi_miqdor
        topildi = True
        break

if topildi:
    with open("imtixon3/products.json", "w") as fayl:
        json.dump(mahsulotlar, fayl, ensure_ascii=False, indent=4)
    print("Miqdor yangilandi.")
else:
    print("Mahsulot topilmadi.")