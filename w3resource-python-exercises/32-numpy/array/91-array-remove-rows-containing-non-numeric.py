import numpy as np

x = np.array([[1,2,3], [4,5,np.nan], [7,8,9], [True, False, True]])
print(x)

x_filtered = x[~np.isnan(x).any(axis=1)]
print(x_filtered)

