import pandas as pd
import numpy as np

values = pd.DataFrame(np.random.randn(10, 2))
print("values:")
print(values)
print()

part_70 = values.sample(frac=0.7,random_state=10)
print("70% of the said DataFrame:")
print(part_70)
print()

part_30 = values.drop(part_70.index)
print("30% of the said DataFrame:")
print(part_30)

