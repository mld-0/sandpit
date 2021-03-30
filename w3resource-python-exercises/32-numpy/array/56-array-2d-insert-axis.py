import numpy as np
x = np.zeros((3, 4))
print(x.shape)
print(x)

print("Expand axis=0")
y = np.expand_dims(x, axis=0)
print(y.shape)
print(y)

print("Expand axis=1")
y = np.expand_dims(x, axis=1)
print(y.shape)
print(y)

print("Expand axis=2")
y = np.expand_dims(x, axis=2)
print(y.shape)
print(y)

