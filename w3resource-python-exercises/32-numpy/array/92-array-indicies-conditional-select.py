import numpy as np

a = np.array([97, 101, 105, 111, 117])
b = np.array(['a','e','i','o','u'])

b_filtered = b[(a > 100) & (a < 110)]

print(b_filtered)


