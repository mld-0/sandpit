import numpy as np
import pandas as pd

values = pd.Series(['Php', 'Python', 'Java', 'C#'])
print("values:")
print(values)

_char_count = lambda x: len(x)

result = values.map(_char_count)
print("result:")
print(result)

