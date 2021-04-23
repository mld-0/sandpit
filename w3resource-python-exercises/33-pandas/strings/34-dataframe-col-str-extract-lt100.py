import pandas as pd
import re as re

pd.set_option('display.max_columns', 10)

values = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'address': ['72 Surrey Ave.11','92 N. Bishop Ave.','9910 Golden Star St.', '102 Dunbar St.', '17 West Livingston Court']
    })

print("values:")
print(values)

def test_num_less(n):
    result = re.findall(r'\b(0*(?:[1-9][0-9]?|100))\b', n)
    return result

values['num_less'] = values['address'].apply(lambda x : test_num_less(x))

print("Number less than 100:")
print(values)

