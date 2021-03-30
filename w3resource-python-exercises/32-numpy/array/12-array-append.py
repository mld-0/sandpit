import numpy as np

x = [10, 20, 30]
print(x)
print()

x_appended = np.append(x, [[40, 50, 60], [70, 80, 90]])
print(x_appended)
print()

x = [[10, 20, 30]]
x_appended = np.append(x, [[40, 50, 60], [70, 80, 90]], axis=0)
print(x_appended)
