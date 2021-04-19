import numpy as np
import pandas as pd
from collections import Counter

_val_str = list('abc def abcdef icd')
values = pd.Series(_val_str)
print("values:")
print(values.to_list())

_least_freq_char = values.value_counts().index[-1]

result = values.replace(' ', _least_freq_char)
print("result:")
print(result.to_list())

