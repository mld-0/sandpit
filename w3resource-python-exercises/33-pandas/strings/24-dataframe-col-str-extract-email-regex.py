import pandas as pd
import re as re

pd.set_option('display.max_columns', 10)

values = pd.DataFrame({
    'name_email': ['Alberto Franco af@gmail.com','Gino Mcneill gm@yahoo.com','Ryan Parkes rp@abc.io', 'Eesha Hinton', 'Gino Mcneill gm@github.com']
})
print("values:")
print(values)

_delim = ","

_email_find = lambda x: _delim.join(re.findall(r'[\w\.-]+@[\w\.-]+', str(x)))

values['extract_email'] = values['name_email'].apply(_email_find)

print("extract_email:")
print(values)

