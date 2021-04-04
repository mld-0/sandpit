import numpy as np

#   Vectors
p = [1, 2, 3]
q = [0, 2, 4]
print("p")
print(p)
print("q")
print(q)
result1 = np.cross(p, q)
result2 = np.cross(q, p)
print("cross product of the said two vectors(p, q):")
print(result1)
print("cross product of the said two vectors(q, p):")
print(result2)
print()

#   Arrays of vectors
p = [[1, 0, 0], [0, 1, 0]]
q = [[1, 2, 0], [3, 4, 0]]
print("p")
print(p)
print("q")
print(q)
result1 = np.cross(p, q)
result2 = np.cross(q, p)
print("cross product of the said two vectors(p, q):")
print(result1)
print("cross product of the said two vectors(q, p):")
print(result2)
print()

#   Where the dimension of the vector is 2, the third component is assumed to be zero. Where both vectors have dimension 2, only the z-component (the only non-zero component) is returned
p = [[1, 0], [0, 1]]
q = [[1, 2], [3, 4]]
print("p")
print(p)
print("q")
print(q)
result1 = np.cross(p, q)
result2 = np.cross(q, p)
print("cross product of the said two vectors(p, q):")
print(result1)
print("cross product of the said two vectors(q, p):")
print(result2)


