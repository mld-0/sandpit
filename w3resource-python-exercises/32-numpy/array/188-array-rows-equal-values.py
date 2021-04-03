import numpy as np

values = np.array([[1,2,3,2], [2,3,4,5], [1,1,2,2], [0,0,1,0], [1,1,1,1], [1,1,2,1], [2,2,2,2]])
print(values)

#print(values[:, :-1])
#print(values[:, 1:])

#   Compare elements of each row, m cols produces m-1 comparisons for each row
values_comp = values[:, :-1] == values[:, 1:]
print(values_comp)

#   result_indices is given by and-ing these comparisons for each row
result_indices = np.logical_and.reduce(values_comp, axis=1)
print(result_indices)

#   result is given by True indicies in result_indices
result = values[result_indices]
print(result)

