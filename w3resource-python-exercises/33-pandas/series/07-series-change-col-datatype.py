import pandas as pd

values = pd.Series(['100', '200', 'python', '300.12', '400'])
print(type(values))
print(values)

result = pd.to_numeric(values, errors='coerce')
print(type(result))
print(result)

