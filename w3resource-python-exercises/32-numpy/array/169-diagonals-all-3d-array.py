import numpy as np

values = np.arange(3*3*3).reshape(3,3,3)
print(values)

result = np.diagonal(values, axis1=1, axis2=2)
print(result)

result = np.diagonal(values, axis1=0, axis2=1)
print(result)

result = np.diagonal(values, axis1=2, axis2=0)
print(result)




