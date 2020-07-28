import time
import datetime
from datetime import date
import calendar

today = datetime.date.today()

print(today)
print(today.day)
print(today.month)
print(today.year)


yy=2019
mm=11
print(calendar.month(yy,mm))

cal=calendar.Calendar()
for x in cal.itermonthdays(2016,5):
    print(x)
