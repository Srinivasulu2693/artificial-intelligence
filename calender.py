import calendar

def generate_calendar(year, month):
    c = calendar.TextCalendar(calendar.SUNDAY)
    return c.formatmonth(year, month)

year = 2022
month = 2
print(generate_calendar(year, month))
