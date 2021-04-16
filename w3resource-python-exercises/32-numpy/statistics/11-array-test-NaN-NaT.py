import numpy as np

print("isfinite")
print(np.isfinite(1))
print(np.isfinite(0))
print(np.isfinite(np.nan))
print()

print("isinf")
print(np.isinf(np.inf))
print(np.isinf(np.nan))
print(np.isinf(np.NINF))
print()

print("isnan")
print(np.isnan([np.log(-1.),1.,np.log(0)]))
print()

print("isnat")
print(np.isnat(np.array(["NaT", "2016-01-01"], dtype="datetime64[ns]")))
print()

print("isneginf")
x = np.array([-np.inf, 0., np.inf])
y = np.array([2, 2, 2])
print(np.isneginf(x, y))
print()

print("isposinf")
x = np.array([-np.inf, 0., np.inf])
y = np.array([2, 2, 2])
print(np.isposinf(x, y))

