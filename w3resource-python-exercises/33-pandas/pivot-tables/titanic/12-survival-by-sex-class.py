import numpy as np
import pandas as pd

_df = pd.read_csv('titanic.csv')
print("_df:")
print(_df)
print()

result = _df.groupby(['sex', 'class'])['survived'].agg('mean')
print("result:")
print(result)
print()

print("result.unstack:")
print(result.unstack())
print()

result_counts = _df.groupby(['sex', 'class'])['survived'].agg('count')
result_survived = _df.groupby(['sex', 'class'])['survived'].agg('sum')
result = result_survived / result_counts
print("result:")
print(result)

