import numpy as np

x = np.array([200, 300, np.nan, np.nan, np.nan ,700])
print(x)

result = x[~np.isnan(x)]
print(result)
print()

y = np.array([[1, 2, 3], [np.nan, 0, np.nan] ,[6,7,np.nan]] )
print(y)

result = y[~np.isnan(y)]
#   or
result = y[np.logical_not(np.isnan(y))]
print(result)
