import numpy as np
import pandas as pd

values = pd.DataFrame(np.random.randint(1,10,(200,40)))
print("values:")
print(values)

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

print("Increase display size:")
print(values)

