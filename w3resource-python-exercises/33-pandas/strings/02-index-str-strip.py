import pandas as pd

values = pd.Index([' Green', 'Black ', ' Red ', 'White', ' Pink '])
print("values:")
print(values)
print()

#   Remote whitespace
result = values.str.strip()
print("result strip():")
print(result)

#   Remove whitespace LHS
result = values.str.lstrip()
print("result lstrip():")
print(result)

#   Remove whitespace RHS
result = values.str.rstrip()
print("result rstrip():")
print(result)

