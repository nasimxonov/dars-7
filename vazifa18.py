from datetime import datetime, timedelta

oylar = [
    "Yanvar",
    "Fevral",
    "Mart",
    "Aprel",
    "May",
    "Iyun",
    "Iyul",
    "Avgust",
    "Sentabr",
    "Oktabr",
    "Noyabr",
    "Dekabr",
]

kunlar = [
    "Dushanba",
    "Seshanba",
    "Chorshanba",
    "Payshanba",
    "Juma",
    "Shanba",
    "Yakshanba",
]

str_time = '2024-09-30 14:45:12'

date = datetime.strptime(str_time, "%Y-%m-%d %H:%M:%S")

date += timedelta(days=7, hours=3, minutes=15)

oy_nomi = oylar[int(date.strftime("%m")) - 1]

kun = kunlar[int(date.strftime("%w")) - 1]

print(date.strftime(f"{kun}, %d-{oy_nomi}-%Y %H:%M:%S"))