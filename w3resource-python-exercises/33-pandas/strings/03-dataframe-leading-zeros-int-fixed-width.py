import pandas as pd

_data = {'amount': [10, 25, 3000, 40000, 5000000]}
values = pd.DataFrame(_data)
print("values:")
print(values)

values['amount'] = values['amount'].apply(lambda x: '{0:0>8}'.format(x))
#   or
values['amount'] = values['amount'].map(str).str.zfill(8)

print("pad integers:")
print(values)


