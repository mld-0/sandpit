import numpy as np

values = np.arange(12).reshape((2,6))
print(values)

result = np.ptp(values)
print("ptp")
print(result)

result = np.ptp(values, axis=0)
print("ptp, axis=0")
print(result)

result = np.ptp(values, axis=1)
print("ptp, axis=1")
print(result)
