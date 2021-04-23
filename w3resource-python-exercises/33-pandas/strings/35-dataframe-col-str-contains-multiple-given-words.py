import pandas as pd
import re as re

pd.set_option('display.max_columns', 10)

values = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'address': ['9910 Surrey Ave.','92 N. Bishop Ave.','9910 Golden Star Ave.', '102 Dunbar St.', '17 West Livingston Court']
    })

print("values:")
print(values)

def test_and_cond(text):
    result = re.findall(r'(?=.*Ave.)(?=.*9910).*', text) 
    return " ".join(result)

values['check_two_words'] = values['address'].apply(lambda x : test_and_cond(x))

print("check_two_words:")
print(values)

