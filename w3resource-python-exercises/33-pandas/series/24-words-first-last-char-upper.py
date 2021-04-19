import numpy as np
import pandas as pd

values = pd.Series(['php', 'python', 'java', 'c#'])
print("values:")
print(values)

_first_last_toupper = lambda x: x[0].upper() + x[1:-1] + x[-1]

result = values.map(_first_last_toupper)
print("result:")
print(result)

