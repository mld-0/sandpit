import numpy as np

values = np.array([[1,0,-1], [0,1,0], [1,0,1]])
print(values)

result = np.linalg.cond(values)
print(result)

