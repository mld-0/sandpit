import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

_df = pd.read_csv('ufo.csv')
_df['length_of_encounter_seconds'] = _df['length_of_encounter_seconds'].astype(str).str.replace('`', '')
_df['duration_min'] = pd.to_numeric(_df['length_of_encounter_seconds']) / 60
print("_df:")
print(_df)

result = _df['duration_min']
result = result.sort_values()
result = result[result < _df['duration_min'].quantile(0.95)]

print("result:")
print(result)
print()

plt.figure(figsize=(10, 8))
sns.distplot(result)

plt.xlabel('Duration(min)', fontsize=20)
plt.ylabel("Frequency", fontsize=15)
plt.xticks(fontsize=12)
plt.title("-Distribution of UFO obervation time-", fontsize=20)
plt.show()

