import numpy as np

nums1 = np.array([0.5, 1.5, 0.23])
nums2 = np.array([0.4999999999, 1.5000000001, 0.23])

np.set_printoptions(precision=15)

print(nums1)
print(nums2)
print(nums1 == nums2)
print(np.equal(nums1, nums2))
