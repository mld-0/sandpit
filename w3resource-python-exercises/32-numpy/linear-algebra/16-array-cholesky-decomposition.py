import numpy as np

values = np.array([[4, 12, -16], [12, 37, -53], [-16, -53, 98]], dtype=np.int32)
print(values)

L = np.linalg.cholesky(values)
print("L")
print(L)

