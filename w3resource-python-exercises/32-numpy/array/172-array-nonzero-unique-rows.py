import numpy as np

values = np.array( [[ 1, 1, 0,], [ 0, 0, 0,], [ 0, 2, 3,], [ 0, 0, 0,], [ 0, -1, 1,], [ 0, 0, 0,]])
print(values)

#   Unique rows 
unique_rows, unique_indexes, unique_counts = np.unique(values, return_index=True, return_counts=True, axis=0)

#   Remove all-zero rows
result_rows = []
for i, unique_row in enumerate(unique_rows):
    if not np.all(unique_row == 0):
        result_rows.append(i)
unique_rows = unique_rows[result_rows]
unique_indexes = unique_indexes[result_rows]
unique_counts = unique_counts[result_rows]

print(unique_rows)
print(unique_indexes)
print(unique_counts)
