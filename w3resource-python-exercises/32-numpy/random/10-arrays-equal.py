import numpy as np

a = np.random.randint(0,10,6)
b = np.random.randint(0,10,6)
print(a)
print(b)

result = np.allclose(a,b)
print(result)

