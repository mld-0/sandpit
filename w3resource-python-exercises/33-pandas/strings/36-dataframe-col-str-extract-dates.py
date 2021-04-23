import pandas as pd
import re as re

values = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'zefsalf', 'svaluesslew', 'zekfsvalues'],
    'date_of_sale': ['12/05/2002','16/02/1999','05/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]
})

print("values:")
print(values)
print()

def find_valid_dates(dt):
    #format: mm-dd-yyyy
    result = re.findall(r'\b(1[0-2]|0[1-9])/(3[01]|[12][0-9]|0[1-9])/([0-9]{4})\b',dt)
    return result

values['valid_dates']=values['date_of_sale'].apply(lambda dt : find_valid_dates(dt))
print("Valid dates (format: mm-dd-yyyy):")
print(values)

