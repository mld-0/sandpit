import numpy as np

x = np.array([-1.6, -1.5, -0.3, 0.1, 1.4, 1.8, 2.0])
print("Original array:")
print(x)

print("Floor values of the above array elements:")
print(np.floor(x))

print("Ceil values of the above array elements:")
print(np.ceil(x))

print("Truncated values of the above array elements:")
print(np.trunc(x))

