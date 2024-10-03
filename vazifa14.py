n = int(input("Son kiriting: "))

if n < 10 or n > 100:
    raise Exception("Son 10 bilan 100 oraligida bolishi kerak")

else:
    print("Togri kiritildi")
