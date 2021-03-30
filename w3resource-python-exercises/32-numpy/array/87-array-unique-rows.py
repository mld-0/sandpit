import numpy as np

x = np.array([[20, 20, 20, 0], [0, 20, 20, 20], [0, 20, 20, 20], [20, 20, 20, 0], [10, 20, 20,20]])

#   w3resource solution:
#print(x)
#y = np.ascontiguousarray(x).view(np.dtype((np.void, x.dtype.itemsize * x.shape[1])))
#print(y)
#_, idx = np.unique(y, return_index=True)
#unique_result = x[idx]
#print(unique_result)

print(x)

rows, row_indexs, row_counts = np.unique(x, return_index=True, return_counts=True, axis=0)
print(row_indexs)
print(row_counts)

#print(rows)
#print(row_indexs)
#print(row_counts)

print("Unique rows")
unique_result = x[row_indexs]
print(unique_result)

print("Unique rows count <= 1")
unique_result = unique_result[row_counts <= 1]
print(unique_result)

