import numpy as np

x = np.array([10, 20, 30], float)
print(x)

s = x.tobytes()
print(s)

y = np.frombuffer(s)
print(y)

