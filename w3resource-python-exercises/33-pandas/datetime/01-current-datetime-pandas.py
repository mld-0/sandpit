import datetime
import numpy as np
import pandas as pd

_today = datetime.date.today()
print("_today:")
print(type(_today))
print(_today)
print()

_today_pandas = pd.to_datetime(_today)
print("_today_pandas:")
print(type(_today_pandas))
print(_today_pandas)

