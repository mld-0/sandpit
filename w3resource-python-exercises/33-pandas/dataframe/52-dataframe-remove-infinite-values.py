import pandas as pd
import numpy as np

values = pd.DataFrame([1000, 2000, 3000, -4000, np.inf, -np.inf])
print("values:")
print(values)

values = values.replace([np.inf, -np.inf], np.nan)
print("Replace Infinite with NaN:")
print(values)

