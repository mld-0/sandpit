import numpy as np

values = np.arange(0,20).reshape(4,5)
print(values)

result = values[:, [3,1,2,0,4]]
print(result)
#   or
result[:, [0,3]] = values[:, [3,0]]
print(result)


