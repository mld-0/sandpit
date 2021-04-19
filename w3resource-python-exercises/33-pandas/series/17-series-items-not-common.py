import numpy as np
import pandas as pd
import inspect

a = pd.Series([1, 2, 3, 4, 5])
b = pd.Series([2, 4, 6, 8, 10])
print("a:")
print(a)
print("b:")
print(b)
print()

#   Using np.union1d() and np.intersect1d() set operations
ab_union = np.union1d(a, b)
print("ab_union:")
print(ab_union)
ab_intersect = np.intersect1d(a, b)
print("ab_intersect:")
print(ab_intersect)
indices_result = ~np.isin(ab_union, ab_intersect)
print("indices_result:")
print(indices_result)
result = ab_union[indices_result]
print("result:")
print(result)
print()

#   Using pandas concat()/unique(), and set operations
ab_union = pd.concat([a, b]).unique()
print("ab_union:")
print(ab_union)
ab_intersect = list(set(a) & set(b))
print("ab_intersect:")
print(ab_intersect)
indices_result = ~pd.Series(ab_union).isin(ab_intersect)
print("indices_result:")
print(indices_result.to_numpy())  # Convert to ndarray for consisetency in output formatting
result = ab_union[indices_result]
print("result:")
print(result)




