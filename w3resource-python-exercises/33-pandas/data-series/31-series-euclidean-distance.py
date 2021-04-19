import numpy as np
import pandas as pd

a = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
b = pd.Series([11, 8, 7, 5, 6, 5, 3, 4, 7, 1])
print("a:")
print(a.to_list())
print("b:")
print(b.to_list())

ab_difference = a - b
print("ab_difference:")
print(ab_difference.to_list())

result = np.linalg.norm(ab_difference)
print("result:")
print(result)


