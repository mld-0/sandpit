import datetime

days = 4
hours = 5
minutes = 20
seconds = 10

delta = datetime.timedelta(days = days, hours = hours, minutes = minutes, seconds = seconds)
print(delta.total_seconds())

