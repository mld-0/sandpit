import datetime
import dateutil.parser

date1 = datetime.datetime(year=2020, month=12, day=25)
print("Date from a given year, month, day:")
print(date1)
print()

date2 = dateutil.parser.parse("1st of January, 2021")
print("Date from a given string formats:")
print(date2)

