import numpy as np
import pandas as pd

_data = {"agent": ["a001", "a002", "a003", "a003", "a004"], "purchase":[4500.00, 7500.00, "$3000.25", "$1250.35", "9000.00"]}
values = pd.DataFrame(_data)
print("values:")
print(values)
print(values.dtypes)
print()

values['purchase'] = values['purchase'].replace("[$,]", "", regex=True).astype(float)
print("cleaned 'purchase', convert to float:")
print(values)
print(values.dtypes)

