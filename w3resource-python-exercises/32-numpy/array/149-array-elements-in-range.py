import numpy as np

values = np.array([1, 3, 7, 9, 10, 13, 14, 17, 29])
print("values")
print(values)

a = 7
b = 20
print("range: [%i, %i]" % (a,b))

result = values[(values >= a) & (values <= b)]
print("result")
print(result)

result_index = np.where((values >= a) & (values <= b))
#   or
result_index = np.where(np.logical_and(values >= a, values <= b))
print("indexes")
print(result_index)

