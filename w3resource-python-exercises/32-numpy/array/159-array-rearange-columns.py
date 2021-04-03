import numpy as np


values = np.array([[11,22,33,44,55], [66,77,88,99,100]])
print(values)

i = [1,3,0,4,2]

result = values[:, i]
print(result)
