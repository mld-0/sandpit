import numpy as np

student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40., 42., 45., 41., 38., 40., 42.0])

#   Sort by height, then by id
_indices = np.lexsort((student_id, student_height))
print("indices")
print(_indices)

student_id_sorted = student_id[_indices]
student_height_sorted = student_height[_indices]

print("id")
print(student_id_sorted)
print("height")
print(student_height_sorted)

#results = np.vstack((student_id[_indices], student_height[_indices]))
#print(results)

