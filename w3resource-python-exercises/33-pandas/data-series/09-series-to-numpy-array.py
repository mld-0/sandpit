import numpy as np
import pandas as pd

values = pd.Series(['100', '200', 'python', '300.12', '400'])
print(type(values))
print(values)
print()

result = np.array(values)
#   or
result = np.array(values.values)
#   or
result = np.array(values.values.tolist())
print(type(result))
print(result)

