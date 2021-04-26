import pandas as pd

dates1 = pd.to_datetime([1329806505, 129806505, 1249892905, 1249979305, 1250065705], unit='s')
print("Convert integer or float epoch times to Timestamp and DatetimeIndex upto second:")
print(dates1)
print()

dates2 = pd.to_datetime([1249720105100, 1249720105200, 1249720105300, 1249720105400, 1249720105500], unit='ms')
print("Convert integer or float epoch times to Timestamp and DatetimeIndex upto milisecond:")
print(dates2)

