import numpy as np
import pandas as pd

sr1 = pd.Series(['php', 'python', 'java', 'c#', 'c++'])
sr2 = pd.Series([1, 2, 3, 4, 5])
print("sr1:")
print(sr1)
print("sr2:")
print(sr2)
print()

values = pd.DataFrame(sr1, sr2).reset_index()
print(values)
print()

values = pd.concat((sr1, sr2), axis=1)
print(values)
print()

values = pd.DataFrame({'col1': sr1, 'col2': sr2})
print(values)

