import pandas as pd
import re as re

pd.set_option('display.max_columns', 10)

values = pd.DataFrame({
    'text_code': ['t0001.','t0002','t0003', 't0004'],
    'text_lang': ['Shee liveddd a long lifee.', 'How oold is your father?', 'What is tthe problem?','TThhis desk is used by Tom.']
})
print("values:")
print(values)
print()

_rep_char = lambda x: x.groups(0)[0]
_unique_char = lambda x: re.sub('r(\w)\1+', _rep_char, x)

values['converted_text'] = values['text_lang'].apply(_unique_char)

print("converted_text:")
print(values)

