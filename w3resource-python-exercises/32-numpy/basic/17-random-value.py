import numpy as np

#   Value from normal distribution
value = np.random.normal(0,1,1)
print(value)

#   Wrapper for np.random.random_sample()
value = np.random.rand()
print(value)

#   Float from [0.0, 1.0)
value = np.random.random()
print(value)

#   Float from standard normal distribution
value = np.random.randn()
print(value)
