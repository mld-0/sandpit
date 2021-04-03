import numpy as np

values = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(values)

result = np.triu(values, 0)
print(result)

result = np.triu(values, -1)
print(result)


