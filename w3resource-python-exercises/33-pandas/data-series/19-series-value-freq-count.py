import numpy as np
import pandas as pd

np.random.seed(0)

values = pd.Series(np.random.randint(0, 10, 20))
values = values.append(pd.Series(['python']))

print("values:")
print(values)

result_count = values.value_counts()
print("result_count:")
print(result_count)

