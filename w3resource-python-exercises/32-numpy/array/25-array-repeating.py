import numpy as np
a = [1, 2, 3, 4]
print("Original array")
print(a)

print("Repeating 2 times")
x = np.tile(a, 2)
print(x)

print("Repeating 3 times")
x = np.tile(a, 3)
print(x)
