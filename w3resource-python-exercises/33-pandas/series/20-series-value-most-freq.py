import numpy as np
import pandas as pd

np.random.seed(0)

values = pd.Series(np.random.randint(0, 10, 20))
values = values.append(pd.Series(['python']))

_most_freq_replace = 'Other'

print("values:")
print(values)

result_count = values.value_counts()
print("result_count:")
print(result_count)

#   Replace all items not equal to the most frequent value with _most_freq_replace
_most_freq = result_count.index[0]
print("_most_freq:")
print(_most_freq)

_indices_most_freq = values == _most_freq
print("_indices_most_freq:")
print(_indices_most_freq.to_numpy())

values[~_indices_most_freq] = _most_freq_replace
print("values, replace ~_indices_most_freq")
print(values)

