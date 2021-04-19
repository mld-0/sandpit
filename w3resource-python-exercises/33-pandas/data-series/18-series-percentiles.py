import pandas as pd
import numpy as np

values = pd.Series(np.arange(1,21))
print("values:")
print(values)

_result_percentiles = [0, 25, 50, 75, 100]
print("_result_percentiles:")
print(_result_percentiles)

#   Using pd.quantile() 
result = values.quantile([x/100 for x in _result_percentiles])  # Convert percentages to decimals for pd.quantile()
print("result:")
print(result)

#   Using np.percentile() 
result_vals = np.percentile(values, _result_percentiles)
result = pd.Series(result_vals, _result_percentiles)  # Convert results to series for consistent formatting
print("result:")
print(result)

