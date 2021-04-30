import numpy as np
import pandas as pd

values = pd.read_excel('coalpublic2013.xlsx', skiprows=3)
print("values:")
print(values)
print()

_sum_row = values[['Production (short tons)', 'Labor Hours']].sum()
print("_sum_row:")
print(type(_sum_row))
print(_sum_row)
print()

values_sum = pd.DataFrame(_sum_row).T

print("values_sum:")
print(type(values_sum))
print(values_sum)
