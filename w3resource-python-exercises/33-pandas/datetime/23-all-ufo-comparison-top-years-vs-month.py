import numpy as np
import pandas as pd

_df = pd.read_csv('ufo.csv')
_df['Date_time'] = _df['Date_time'].str.replace('24:', '00:')
_df['Date_time'] = pd.to_datetime(_df['Date_time'], format='%m/%d/%Y %H:%M')
print("_df:")
print(_df)
print()

_top_years = _df['Date_time'].dt.year.value_counts().head(10)
print("_top_years:")
print(_top_years)
print()

_is_top_year = lambda x: x if x in _top_years.index else None

month_vs_year = pd.pivot_table(_df, columns=_df['Date_time'].dt.month, index=_df['Date_time'].dt.year.apply(_is_top_year), values='city', aggfunc='count')
month_vs_year.index = month_vs_year.index.astype(int)
month_vs_year.columns = month_vs_year.columns.astype(int)

print("month_vs_year:")
print(month_vs_year)


