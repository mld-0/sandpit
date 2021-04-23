import pandas as pd

values = pd.DataFrame({
    'company_code': ['Company','Company a001', '2055', 'abcd', '123345'],
    'date_of_sale ': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})
	
print("values:")
print(values)
print()

values['check_code_is_digit'] = values['company_code'].str.isdigit()
#   or
values['check_code_is_digit'] = values['company_code'].apply(lambda x: x.isdigit())

print("values:")
print(values)

