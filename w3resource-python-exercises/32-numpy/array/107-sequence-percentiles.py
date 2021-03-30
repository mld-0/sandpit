import numpy as np

nums = np.array([1,2,3,4,5])

print("50th percentile (median):")
p = np.percentile(nums, 50)
print(p)

print("40th percentile:")
p = np.percentile(nums, 40)
print(p)

print("90th percentile:")
p = np.percentile(nums, 90)
print(p)

