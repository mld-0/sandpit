import numpy as np
import pandas as pd

values = pd.Series(['X', 'Y', 'Z', 'Aaba', 'Baca', np.nan, 'CABA', None, 'bird', 'horse', 'dog'])
print("values:")
print(values)


result_len = values.str.len()
#   or
result_len = values.apply(lambda x: len(x) if type(x) is str else np.nan)
print("result_len:")
print(result_len)

result_upper = values.str.upper()
print("result_upper:")
print(result_upper)

result_lower = values.str.lower()
print("result_lower:")
print(result_lower)

result_capitalize = values.str.capitalize()
print("result_capitalize:")
print(result_capitalize)

result_swapcase = values.str.swapcase()
print("result_swapcase:")
print(result_swapcase)

