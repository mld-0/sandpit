import pandas as pd

_dt_range = pd.date_range(start='2020-05-12 07:10:10', freq='S', periods=10)
values = pd.DataFrame({"Sale_amt":[100, 110, 117, 150, 112, 99, 129, 135, 140, 150]}, index = _dt_range)
print("values:")
print(values)
