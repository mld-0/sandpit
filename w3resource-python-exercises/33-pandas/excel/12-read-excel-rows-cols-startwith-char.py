import numpy as np
import pandas as pd

values = pd.read_excel('coalpublic2013.xlsx', skiprows=3)
print("values:")
print(values)
print()

_startswith_P = lambda x: x.startswith('P') 

_result_indices = values['Mine Name'].astype(str).map(_startswith_P)
print("_result_indices:")
print(_result_indices)
print()

result = values[_result_indices]
print("result:")
print(result)

