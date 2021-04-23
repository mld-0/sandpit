import pandas as pd

values = pd.DataFrame({
    'company_code': ['ABCD','EFGF', 'hhhh', 'abcd', 'EAWQaaa'],
    'date_of_sale ': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})

print("values:")
print(values)
print()

results_islower= values['company_code'].str.islower()
#   or
results_islower = values['company_code'].apply(lambda x: x.islower())

results_isupper = values['company_code'].str.isupper()
#   or
results_isupper = values['company_code'].apply(lambda x: x.isupper())

print("results_islower:")
print(results_islower)
print("results_isupper:")
print(results_isupper)


