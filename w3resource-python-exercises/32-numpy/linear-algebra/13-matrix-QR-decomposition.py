import numpy as np

values = np.array([[1,2],[3,4]])
print(values)

Q, R = np.linalg.qr(values)
print("Q")
print(Q)
print("R")
print(R)

