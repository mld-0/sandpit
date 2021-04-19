import numpy as np
import pandas as pd

values = pd.Series(np.arange(8), index=list('ABCDEFGH'))
print("values:")
print(values)

result = values.to_frame().reset_index()
print("result:")
print(result)

