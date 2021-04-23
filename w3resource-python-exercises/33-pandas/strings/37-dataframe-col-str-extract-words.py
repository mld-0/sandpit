import pandas as pd
import re as re

values = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'zefsalf', 'svaluesslew', 'zekfsvalues'],
    'date_of_sale': ['12/05/2002','16/02/1999','05/09/1998','12/02/2022','15/09/1997'],
    'address': ['9910 Surrey Ave.','92 N. Bishop Ave.','9910 Golden Star Ave.', '102 Dunbar St.', '17 West Livingston Court']
})

print("values:")
print(values)
print()

def search_words(text):
    result = re.findall(r'\b[^\d\W]+\b', text)
    return " ".join(result)

values['only_words'] = values['address'].apply(lambda x : search_words(x))

print("Only words:")
print(values)

