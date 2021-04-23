import pandas as pd
values = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'zefsalf', 'svaluesslew', 'zekfsvalues'],
    'date_of_sale': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]
})
print("values:")
print(values)
print()

_substr = 'ze'
print("_substr:")
print(_substr)
print()

values['company_code_starts_with'] = values['company_code'].str.startswith(_substr)
#   or
values['company_code_starts_with'] = values['company_code'].apply(lambda x: x.startswith(_substr))

print("company_code_starts_with:")
print(values)

