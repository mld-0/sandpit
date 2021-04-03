import numpy as np

x = np.array([10,-10,10,-10,-10,10])
y = np.array([.85,.45,.9,.8,.12,.6])
print(x)
print(y)

result = np.sum((x == 10) & (y > .5))
print(result)
