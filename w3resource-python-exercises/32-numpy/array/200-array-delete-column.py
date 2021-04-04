import numpy as np

values = np.random.randint(0, 10, (7,5))
print(values)

#   Copy of array without first column
result = np.delete(values, [0], axis=1)
print(result.shape)
print(result)
print("Shares memory: ", np.shares_memory(values, result))

#   Copy of array without last column
result = np.delete(values, [-1], axis=1)
print(result.shape)
print(result)

#   View of array with last copy removed
result = values[:, 0:-1]
print(result.shape)
print(result)
print("Shares memory: ", np.shares_memory(values, result))

