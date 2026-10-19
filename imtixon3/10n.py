import matplotlib.pyplot as plt

kunlar = ["Du", "Se", "Cho", "Pay", "Ju", "Sha", "Yak"]
daromad = [120, 150, 100, 180, 200, 240, 210]

plt.plot(kunlar, daromad)
plt.title("7 Yetti kunlik daromat")
plt.xlabel("Hafta kunlari")
plt.ylabel("Hafta daromadlari")

plt.show()