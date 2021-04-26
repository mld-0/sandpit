import numpy as np
import pandas as pd

_data = np.random.randint(1,10, (36))
_period_range = pd.period_range('2029-01-01', '2031-12-31', freq='M')

values = pd.Series(_data, _period_range)
print("values:")
print(values)
print()

print("values['2030']:")
print(values['2030'])

