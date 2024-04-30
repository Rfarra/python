import calendar

print(calendar.calendar(2024))
print(calendar.month(2024, 1))
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.month(2024, 1))
print(calendar.weekday(2024, 1, 1))
print(calendar.weekheader(3))
print(calendar.isleap(2024))
print(calendar.leapdays(2000, 2024))
cal = calendar.Calendar()
