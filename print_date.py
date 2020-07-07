import calendar

c=calendar.TextCalendar(calendar.MONDAY)
dates=c.prmonth(2020,7)
print(dates)

print('*'*100)
dates_=c.promonth(2020,8)
print(dates_)
