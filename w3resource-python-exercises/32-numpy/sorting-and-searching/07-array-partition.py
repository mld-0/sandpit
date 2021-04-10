import numpy as np

values = np.array([70, 50, 20, 30, -11, 60, 50, 40])
print("values")
print(values)

_index = 3
print("index")
print(_index)
print("values[index]")
print(values[_index])

result = np.partition(values, _index)
print("result")
print(result)

