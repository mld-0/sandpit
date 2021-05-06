import numpy as np
import pandas as pd

_df = pd.read_csv('ufo.csv')
_df['Date_time'] = _df['Date_time'].str.replace('24:', '00:')
_df['Date_time'] = pd.to_datetime(_df['Date_time'], format='%m/%d/%Y %H:%M')
print("_df:")
print(_df)
print()

most_sightings_years = _df['Date_time'].dt.year.value_counts().head(10)
print("most_sightings_years:")
print(most_sightings_years)
print()

_is_top_year = lambda x: x in most_sightings_years

_top_years = _df['Date_time'][_df['Date_time'].dt.year.apply(_is_top_year)].dt.year
print("_top_years:")
print(_top_years)
print()

hour_v_year = pd.pivot_table(_df, values=['city'], columns=_df['Date_time'].dt.hour, index=_top_years, aggfunc='count')
hour_v_year.columns = hour_v_year.columns.droplevel().astype(str) + ":00"
hour_v_year.index = hour_v_year.index.astype(int).astype(str)

print("hour_v_year:")
print(hour_v_year)
print()

hour_v_year['sum'] = hour_v_year.sum(axis=1)
hour_v_year_cols_sum = hour_v_year.sum(axis=0)
hour_v_year_cols_sum.name = 'sum'
hour_v_year = hour_v_year.append(hour_v_year_cols_sum)

print("hour_v_year:")
print(hour_v_year)
