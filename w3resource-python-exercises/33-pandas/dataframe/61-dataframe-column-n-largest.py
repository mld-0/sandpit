import pandas as pd

_data = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}
values = pd.DataFrame(_data)
print("values:")
print(values)

_n = 3
print("_n:")
print(_n)

results_col1 = values.nlargest(_n, 'col1')
print("results_col1:")
print(results_col1)

results_col2 = values.nlargest(_n, 'col2')
print("results_col2:")
print(results_col2)

results_col3 = values.nlargest(_n, 'col3')
print("results_col3:")
print(results_col3)



