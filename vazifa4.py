matn = input("Nimadir kiriting: ")

with open("nimadir.txt",mode = "w+") as file:
    file.write(matn)


with open("nimadir.txt", mode = "r+") as file:

    text = file.read().split(' ')

    text.sort(key=len, reverse=True)

    print("Eng kichik soz: ",min(text))
    print("Eng katta soz: ",max(text))