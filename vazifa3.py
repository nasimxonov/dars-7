matn = input("Nimadir kiriting: ")

with open("nimadir.txt",mode = "w+") as file:
    file.write(matn)


with open("nimadir.txt", mode = "r+") as file:
    print("Belgilar nechtaligi: ",len(file.read()))
