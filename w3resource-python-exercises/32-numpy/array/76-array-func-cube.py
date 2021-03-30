import numpy as np

def cube_alt(values):
    _it = np.nditer([values, None])
    #print(_it.operands)
    for a, b in _it:
        b[...] = a*a*a
    #print(_it.operands)
    return _it.operands[1]

def cube(values):
    result = np.power(values, 3)
    return result

values = [1, 2, 3]
print(values)

result = cube(values)
print(result)

result = cube_alt(values)
print(result)



