import numpy as np

values = np.array([24, 27, 30, 29, 18, 14])
print("values")
print(values)

values_argsort = np.argsort(values)
print("argsort")
print(values_argsort)

rankings = np.empty_like(values_argsort)
rankings[values_argsort] = np.arange(len(values))
print("rankings")
print(rankings)

print("sorted")
print(values[values_argsort])
