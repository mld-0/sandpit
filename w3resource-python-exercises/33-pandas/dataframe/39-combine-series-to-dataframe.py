import pandas as pd
import numpy as np

s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
s2 = pd.Series(['10', '20', 'php', '30.12', '40'])
print("s1:")
print(s1)
print("s2:")
print(s2)

#   Combine Series into single column
result = pd.concat([s1, s2], axis=0)
print("result:")
print(result)

#   Combine Series into multiple columns
result = pd.concat([s1, s2], axis=1)
print("result:")
print(result)


