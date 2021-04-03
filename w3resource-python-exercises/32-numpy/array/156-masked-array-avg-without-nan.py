import numpy as np

values = np.array([[10, 20 ,30], [40, 50, np.nan], [np.nan, 6, np.nan], [np.nan, np.nan, np.nan]])
print(values)

values_masked = np.ma.masked_array(values, np.isnan(values))

result = np.mean(values_masked, axis=1)
print(result.filled(np.nan))

