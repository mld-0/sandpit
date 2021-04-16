import numpy as np

values = np.arange(12).reshape((2,6))
print(values)

n = 80
print("percentile %s" % n)
result = np.percentile(values, n)
print(result)

print("percentile %s, axis=0" % n)
result = np.percentile(values, n, axis=0)
print(result)

print("percentile %s, axis=1" % n)
result = np.percentile(values, n, axis=1)
print(result)

