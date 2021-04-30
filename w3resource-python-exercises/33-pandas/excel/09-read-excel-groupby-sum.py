import numpy as np
import pandas as pd

values = pd.read_excel('coalpublic2013.xlsx', skiprows=3)
print("values:")
print(values)
print()

result = values[['MSHA ID', 'Labor Hours']].groupby('MSHA ID').sum()
print("result:")
print(result)

