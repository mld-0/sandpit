import datetime

print("datetime.datetime object for Jan 11 2012:")
print(datetime.datetime(2012, 1, 11))
print()

print("Specific date and time of 9:20 pm") 
print(datetime.datetime(2011, 1, 11, 21, 20))
print()

print("Local date and time:")
print(datetime.datetime.now())
print()

print("A date without time: ")
print(datetime.datetime.date(datetime.datetime(2012, 5, 22)))
print()

print("Current date:")
print(datetime.datetime.now().date())
print()

print("Time from a datetime.datetime:")
print(datetime.datetime.time(datetime.datetime(2012, 12, 15, 18, 12)))
print()

print("Current local time:") 
print(datetime.datetime.now().time())

