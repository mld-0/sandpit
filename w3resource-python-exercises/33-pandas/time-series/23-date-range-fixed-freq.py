import pandas as pd

print("Sequences of fixed-frequency dates and time spans (1 H):")
r1 = pd.date_range('2030-01-01', periods=10, freq='H')
print(r1)
print()

print("Sequences of fixed-frequency dates and time spans (3 H):")
r2 = pd.date_range('2030-01-01', periods=10, freq='3H')
print(r2)

