import numpy as np

values = np.random.randint(0, 10, 10)
print(values)

_values_bincount = np.bincount(values)
#print(_values_bincount)

_values_most_frequent = _values_bincount.argmax()
print("Most frequent")
print(_values_most_frequent)
print("Count")
print(_values_bincount[_values_most_frequent])

