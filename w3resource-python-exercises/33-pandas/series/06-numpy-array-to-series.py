import numpy as np
import pandas as pd

values = np.array([10, 20, 30, 40, 50])
print(type(values))
print(values)

result = pd.Series(values)
print(type(result))
print(result)

