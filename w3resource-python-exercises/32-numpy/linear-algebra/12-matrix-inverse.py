import numpy as np

values = np.array([[1,2],[3,4]])
print(values)

result = np.linalg.inv(values)
print("inverse")
print(result)

result = np.linalg.pinv(values)
print("pseudoinverse")
print(result)

