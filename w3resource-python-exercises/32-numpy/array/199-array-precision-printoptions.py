import numpy as np

nums = np.array([1.2e-7, 1.5e-6, 1.7e-5])
print(nums)

np.set_printoptions(precision=10)
print(nums)

np.set_printoptions(suppress=True, precision=10)
print(nums)




