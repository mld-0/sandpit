import pandas as pd

data1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                      'B': ['B0', 'B1', 'B2']},
                     index=['K0', 'K1', 'K2'])

data2 = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])

print("data1:")
print(data1)
print("data2:")
print(data2)
print()

result = data1.join(data2)
print("result, data1.join(data2):")
print(result)
print()

result = data2.join(data1)
print("result, data2.join(data1):")
print(result)

