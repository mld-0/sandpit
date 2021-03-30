import numpy as np

values = np.array([10, 10, 20, 10, 20, 20, 20, 30, 30, 50, 40, 40])
print(values)

values_freq, values_uniq = np.unique(values, return_counts=True)
print(values_freq)
print(values_uniq)

#   As dict
values_freq_dict = dict(zip(values_freq.tolist(), values_uniq.tolist()))
print(values_freq_dict)
