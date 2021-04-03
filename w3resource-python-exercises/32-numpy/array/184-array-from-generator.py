import numpy as np

def values_generate():
    for n in range(15):
        yield n

values = np.fromiter(values_generate(), dtype=float, count=-1)
print(values)

values = np.fromiter(values_generate(), dtype=float, count=5)
print(values)






