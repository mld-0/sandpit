import pandas as pd
import re as re

values = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'zefsalf', 'svaluesslew', 'zekfsvalues'],
    'date_of_sale': ['12/05/2002','16/02/1999','05/09/1998','12/02/2022','15/09/1997'],
    'address': ['9910 Surrey <b>Avenue</b>','92 N. Bishop Avenue','9910 <br>Golden Star Avenue', '102 Dunbar <i></i>St.', '17 West Livingston Court']
})
print("values:")
print(values)
print()

def remove_tags(string):
    result = re.sub('<.*?>','',string)
    return result

values['with_out_tags'] = values['address'].apply(lambda x : remove_tags(x))
print("Sentences without tags':")
print(values)

