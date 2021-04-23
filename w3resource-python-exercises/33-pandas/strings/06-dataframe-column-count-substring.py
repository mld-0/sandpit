import pandas as pd

values = pd.DataFrame({
    'name_code': ['c001','c002','c022', 'c2002', 'c2222'],
    'date_of_birth ': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'age': [18.5, 21.2, 22.5, 22, 23]
})
print("values:")
print(values)

_substr = "2"
print("_substr:", _substr)

values['count'] = values['name_code'].apply(lambda x: x.count(_substr))
#   or
values['count'] = values['name_code'].str.count(_substr)

print("count _substr:")
print(values)
