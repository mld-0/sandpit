import numpy as np

x = np.array([1, 2, 3, 4, 5, 6])
x_str = x.tobytes()
y = np.frombuffer(x_str, dtype=x.dtype)

print(type(x_str))
print(x_str)

print(x)
print(y)
