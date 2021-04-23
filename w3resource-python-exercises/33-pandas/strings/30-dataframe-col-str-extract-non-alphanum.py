import pandas as pd
import re as re

pd.set_option('display.max_columns', 10)

values = pd.DataFrame({
    'company_code': ['c0001#','c00@0^2','$c0003', 'c0003', '&c0004'],
    'year': ['year 1800','year 1700','year 2300', 'year 1900', 'year 2200']
})

print("values:")
print(values)

_find_nonalpha = lambda x: re.findall("[^A-Za-z0-9]", x)

values['extract_nonalpha'] = values['company_code'].apply(_find_nonalpha)

print("Extracting only non alphanumeric characters from company_code:")
print(values)

