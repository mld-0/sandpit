import numpy as np

a = np.array([[1, 0, 0, 0, 2], [0, 0, 3, 0, 0], [0, 0, 0, 0, 0], [0, 2, 0, 0, 0]], dtype=np.float32)
print(a)

U, s, V = np.linalg.svd(a, full_matrices=False)
print("U")
print(U)
print("s")
print(s)
print("V")
print(V)

