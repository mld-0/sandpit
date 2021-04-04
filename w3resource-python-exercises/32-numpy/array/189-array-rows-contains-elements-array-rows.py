import numpy as np

#   w3resource solution is incorrect - it combines count from each row-in-b, meaning rows in a with multiple matches from a single row in b are identified as solutions

a = np.array([[5, 2, 5, 1,], [5, 4, 1, 3,], [0, 1, 1, 1,], [2, 0, 4, 0,]])
b = np.array([[2, 3,], [1, 4,]])
print(a)
print(b)
print()

#print(a[:, :, None, None])
#print(a[..., None, None])

#print(a[:, :, None, None].shape)
#print(b.shape)

#   For each element in a, does that match each of values in b
#   ab_elements_comparison has a matrix for each element in a, whether that element matches each one of the values in b
ab_elements_comparison = a[:, :, None, None] == b
#print(ab_elements_comparison)

#   Sum (count) the number of matches, resulting in a count for each row in a, how many matches are in b
#print(ab_elements_comparison.sum(axis=1))
#print(ab_elements_comparison.sum(axis=(1,2)))
#print(ab_elements_comparison.sum(axis=(1,2,3)))

#   for each row in a, how many elements from each row in b
a_row_contains_b_count = ab_elements_comparison.sum(axis=(1,3))
print(a_row_contains_b_count)

#   get indices of rows in a_row_contains_b_count where both values are > 0
#   these are the rows in a containing elements from both rows in b
a_row_contains_all_rows_b = np.logical_and.reduce(a_row_contains_b_count, axis=1).nonzero()[0]
print(a_row_contains_all_rows_b)

result = a[a_row_contains_all_rows_b]
print(result)

