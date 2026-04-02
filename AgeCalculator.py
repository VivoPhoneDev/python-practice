import datetime as dt
year = int(input("year: "))
month = int(input("month: "))
day = int(input("day: "))
now = dt.datetime.now()

br = dt.datetime(year, month, day)
age = now.year - br.year
if (now.month, now.day) < (br.month, br.day):
    age -= 1

print("Вам:", age)