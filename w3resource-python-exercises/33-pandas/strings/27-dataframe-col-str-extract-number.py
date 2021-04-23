import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
values = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'address': ['7277 Surrey Ave.','920 N. Bishop Ave.','9910 Golden Star St.', '25 Dunbar St.', '17 West Livingston Court']
    })

print("values:")
print(values)
print()

def find_number(text):
    num = re.findall(r'[0-9]+',text)
    return " ".join(num)

values['number'] = values['address'].apply(lambda x: find_number(x))

print("find number:")
print(values)

