import numpy as np
import pandas as pd

a = pd.Series(np.arange(10))
b = pd.Series(list('pqrstuvwxyz'))
print("a:")
print(a)
print("b:")
print(b)

#   Combine as row
result_h = a.append(b)
#   or
result_h = pd.concat([a, b], axis=0)
print("result_h:")
print(result_h)

#   Combine as columns
result_v = pd.concat([a, b], axis=1)
print("result_v:")
print(result_v)

