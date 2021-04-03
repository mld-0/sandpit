import numpy as np

values = np.arange(1,9)
print(values)

a = 0
n = 2

result = np.zeros(len(values) + (len(values)-1)*n)
result[::n+1] = values

print(result)

