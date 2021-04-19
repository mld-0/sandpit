import pandas as pd

values = pd.Series([0,1,2,3,4,5,6,7,8,9])
print("values:")
print(values)

n_min = 2
n_max = 6
print("n range: [%i, %i]" % (n_min, n_max))

result = values[(values < n_max) & (values > n_min)]
print("result:")
print(result)

