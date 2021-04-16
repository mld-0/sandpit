import numpy as np

values = np.arange(4).reshape((2,2))
print(values)

result_max = np.amax(values)
print("max")
print(result_max)

result_min = np.amin(values)
print("min")
print(result_min)

