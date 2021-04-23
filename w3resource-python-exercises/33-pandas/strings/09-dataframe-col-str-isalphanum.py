import pandas as pd

_data = pd.DataFrame({
    'name_code': ['Company','Company a001','Company 123', '1234', 'Company 12'],
    'date_of_birth ': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'age': [18.5, 21.2, 22.5, 22, 23]
})

values = pd.DataFrame(_data)
print("values:")
print(values)

values['name_code_isalphanum'] = values['name_code'].str.isalnum()
#   or
values['name_code_isalphanum'] = values['name_code'].apply(lambda x: x.isalnum())

print("Check isalphanumeric:")
print(values)

