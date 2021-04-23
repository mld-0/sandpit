import pandas as pd
import re as re

pd.set_option('display.max_columns', 10)

values = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'year': ['year 1800','year 1700','year 2300', 'year 1900', 'year 2200']
})
print("values:")
print(values)
print()

_find_year = lambda x: re.findall(r"\b(18[0-9]{2}|19[0-8][0-9]|199[0-9]|2[01][0-9]{2}|2200)\b", x)

values['year_range'] = values['year'].apply(_find_year)

print("Extracting year between 1800 to 2200:")
print(values)

