import numpy as np

values = np.random.randint(0,10,1000)
print(values)

result_mean = values.mean()
result_var = values.var()
result_std = values.std()

print(result_mean)
print(result_var)
print(result_std)

