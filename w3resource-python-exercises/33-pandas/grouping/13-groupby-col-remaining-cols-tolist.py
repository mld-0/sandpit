import numpy as np
import pandas as pd

values = pd.DataFrame( {'X' : [10, 10, 10, 20, 30, 30, 10], 'Y' : [10, 15, 11, 20, 21, 12, 14], 'Z' : [22, 20, 18, 20, 13, 10, 0]})
print("values:")
print(values)
print()

result = values.groupby(['X']).aggregate(lambda x: x.tolist())
print("result:")
print(result)

