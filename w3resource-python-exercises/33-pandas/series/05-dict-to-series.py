import pandas as pd

values = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
print(type(values))
print(values)

result = pd.Series(values)
print(type(result))
print(result)

