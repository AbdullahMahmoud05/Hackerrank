import calendar

month, day, year = map(int, input().split())

daynum = calendar.weekday(year, month, day)

spacday = calendar.day_name[daynum].upper()

print(spacday)
