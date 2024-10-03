imya = input("Ismingizni kiriting!!! ")
malumot = input("Yana boshqa malumotlaringizni kiriting: ")

with open(f"{imya}.txt", mode="w") as file:

    file.write(imya)
    file.write(malumot)
