import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

values = pd.DataFrame({
'salesman_id': [5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012],
'sale_jan':[150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 1760, 2983.43, 480.4,  1250.45, 75.29,1045.6]})

print("values:")
print(values)
print()

_cut_bins = pd.cut(values['salesman_id'], bins=[0, 5006, np.inf], labels=['S1', 'S2'])
print("_cut_bins:")
print(_cut_bins)
print()

results = values.groupby(_cut_bins)['sale_jan'].sum().reset_index()
print("results:")
print(results)

