import numpy as np

values = [1, 2.71828183, 7.3890561 ]
print(values)

result = np.log(values)
print("ln")
print(result)

result = np.log10(values)
print("log10")
print(result)

result = np.log2(values)
print("log2")
print(result)

n = 3
result = np.log(values) / np.log(n)
print("log%s" % n)
print(result)

