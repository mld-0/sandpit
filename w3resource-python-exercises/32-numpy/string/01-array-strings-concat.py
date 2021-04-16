import numpy as np

x1 = np.array(['Python', 'PHP'], dtype=np.str_)
x2 = np.array(['Java', 'C++'], dtype=str)
print(x1)
print(x2)

result = np.char.add(x1, x2)
print(result)

