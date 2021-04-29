import numpy as np
import pandas as pd

values = pd.DataFrame({ 'id': [1, 1, 2, 3, 3, 4, 4, 4], 'value': ['a', 'a', 'b', None, 'a', 'a', None, 'b'] })
print("values:")
print(values)
print()

result_unique_count = values.groupby('value').nunique()
print("result_unique_count:")
print(result_unique_count)

