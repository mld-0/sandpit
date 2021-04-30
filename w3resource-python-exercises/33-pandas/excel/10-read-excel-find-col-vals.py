import numpy as np
import pandas as pd

values = pd.read_excel('coalpublic2013.xlsx', skiprows=3)
print("values:")
print(values)
print()

result = values[values['MSHA ID'] == 102901]
print("result:")
print(result)

