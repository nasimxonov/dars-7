from datetime import datetime
import calendar

sana = input("Sana kiriting (2024-09-30 14:45:12 ga oxshatib): ")

sana = datetime.strptime(sana, "%Y-%m-%d %H:%M:%S")

oy = calendar.month_name[sana.month]

natija = sana.strftime(f"%d/{oy}/%Y, soat %I:%M:%S %p")
print(natija)
