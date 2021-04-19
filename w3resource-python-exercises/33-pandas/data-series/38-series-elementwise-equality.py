import numpy as np
import pandas as pd

a = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
b = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
print("a:")
print(a)
print("b:")
print(b)

result = a == b
#   or
result = a.eq(b)
print("result:")
print(result)

