import numpy as np

values = np.arange(4).reshape((2,2))
print(values)

print("axis=0")
result_max = np.amax(values, axis=0)
print("max")
print(result_max)
result_min = np.amin(values, axis=0)
print("min")
print(result_min)

print("axis=1")
result_max = np.amax(values, axis=1)
print("max")
print(result_max)
result_min = np.amin(values, axis=1)
print("min")
print(result_min)


