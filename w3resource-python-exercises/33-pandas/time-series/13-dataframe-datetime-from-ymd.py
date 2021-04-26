import pandas as pd

values = pd.DataFrame({'year': [2018, 2019, 2020],
                   'month': [2, 3, 4],
                   'day': [4, 5, 6],
                   'hour': [2, 3, 4]})

print("values:")
print(values)
print()

result = pd.to_datetime(values)
print("result:")
print(result)
print()

result_dates = pd.to_datetime(values[['year', 'month', 'day']])
print("result_dates:")
print(result)

