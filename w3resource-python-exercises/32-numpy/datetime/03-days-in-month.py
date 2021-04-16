import numpy as np

print("Number of days, February, 2015: ")
result = np.datetime64('2015-03-01') - np.datetime64('2015-02-01')
print(result)

print("Number of days, February, 2016: ")
result = np.datetime64('2016-03-01') - np.datetime64('2016-02-01')
print(result)

print("Number of days, February, 2017: ")
result = np.datetime64('2017-03-01') - np.datetime64('2017-02-01')
print(result)

