import pandas as pd

_alcohol_data = pd.read_csv('world_alcohol.csv')
print("_alcohol_data:")
print(_alcohol_data)
print()

_filter_regions = ['Africa', 'Eastern Mediterranean', 'Europe']
print("_filter_regions:")
print(_filter_regions)
print()

_indices_results = _alcohol_data['WHO region'].isin(_filter_regions)
results = _alcohol_data[_indices_results]
print("results:")
print(results)
