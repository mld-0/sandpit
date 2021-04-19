import pandas as pd

values = pd.Series([1, 2, 3, 4, 5], index=['A', 'B', 'C', 'D', 'E'])
print("values:")
print(values)

new_index = ['B', 'A', 'C', 'D', 'E']
print("reindex, new_index:")
print(new_index)

result = values.reindex(index=new_index)
print("result:")
print(result)

