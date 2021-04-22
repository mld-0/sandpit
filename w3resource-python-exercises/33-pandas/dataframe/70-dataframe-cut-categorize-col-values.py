import pandas as pd

values = pd.DataFrame({ 'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Syed Wharton', 'Kierra Gentry'], 'age': [18, 22, 85, 50, 80, 5] })
print("values:")
print(values)

_age_groups = [0, 18, 65, 99]
_age_labels = ['kids', 'adults', 'elderly']

values['age_group'] = pd.cut(values['age'], bins=_age_groups, labels=_age_labels)

print("categorize age_group:")
print(values['age_group'])
print(values['age_group'].dtypes)

