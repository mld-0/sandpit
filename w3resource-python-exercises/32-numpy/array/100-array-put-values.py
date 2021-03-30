import numpy as np

x = np.array([10, 10, 20, 30, 30], float)
print(x)

y = np.array([0, 40, 60], float) 
print(y)

x.put([0, 4], y)
print(x)

