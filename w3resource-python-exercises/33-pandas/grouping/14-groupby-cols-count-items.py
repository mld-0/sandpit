import numpy as np
import pandas as pd

values = pd.DataFrame( {'id' : [1, 2, 1, 1, 2, 1, 2], 'type' : [10, 15, 11, 20, 21, 12, 14], 'book' : ['Math','English','Physics','Math','English','Physics','English']})
print("values:")
print(values)
print()

result = values.groupby(['id', 'type', 'book']).size()
print("result:")
print(type(result))
print(result)
print("result.index:")
print(result.index)
print()

result_unstacked = result.unstack(fill_value=0)
print("result_unstacked:")
print(type(result_unstacked))
print(result_unstacked)
print("result_unstacked.index:")
print(result_unstacked.index)

