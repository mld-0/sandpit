import pandas as pd

result = pd.timedelta_range(0, periods=30, freq='1H20T')
print("result:")
print(result)

