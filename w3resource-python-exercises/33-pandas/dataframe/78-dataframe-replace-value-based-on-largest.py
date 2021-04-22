import numpy as np
import pandas as pd

values = pd.DataFrame({'rnum':[23, 21, 27, 22, 34, 33, 34, 31, 25, 22, 34, 19, 31, 32, 19]})
print("values:")
print(values)
print()

_cummax = values['rnum'].cummax()
print("_cummax:")
print(_cummax)
print()

_eq_cummax = values['rnum'].eq(_cummax)
print("_eq_cummax:")
print(_eq_cummax)
print()

#   Replace values not equal to current largest cumulative value with zero
result = values['rnum'].where(_eq_cummax, 0)
print("result:")
print(result)

