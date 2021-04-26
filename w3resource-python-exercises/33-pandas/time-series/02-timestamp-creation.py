import pandas as pd

print("A specific date using timestamp:")
print(pd.Timestamp('2016-11-10'))
print()

print("Date and time using timestamp:")
print(pd.Timestamp('2012-05-03 11:30'))
print()

print("A time adds in the current local date using timestamp:")
print(pd.Timestamp('11:30'))
print()

print("Current date and time using timestamp:")
print(pd.Timestamp("now"))

