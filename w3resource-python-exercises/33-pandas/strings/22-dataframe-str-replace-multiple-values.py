import pandas as pd

values = pd.DataFrame({
    'company_code': ['A','B', 'C', 'D', 'A'],
    'date_of_sale': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]
})

print("values:")
print(values)
print()

values = values.replace(["A", "D"], ["X", "Y"])
print("Replace [A, D] with [X, Y]:")
print(values)

