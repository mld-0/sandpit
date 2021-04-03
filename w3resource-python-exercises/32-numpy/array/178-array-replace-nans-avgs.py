import numpy as np

a = np.arange(20).reshape(4,5)
print(a)

a_avg = np.mean(a)
print(a_avg)

b = np.array([[1,2,np.nan], [4,5,6], [np.nan, 7, np.nan]])
print(b)

b[np.isnan(b)] = a_avg
print(b)
