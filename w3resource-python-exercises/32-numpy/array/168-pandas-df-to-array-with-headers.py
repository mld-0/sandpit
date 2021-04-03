import numpy as np
import pandas as pd

values = np.random.rand(12,3)
print(type(values))
print(values)

values_df = pd.DataFrame(values, columns=['A', 'B', 'C'])
print(type(values_df))
print(values_df)

