import numpy as np

udict = {"column0":{"a":1,"b":0.0,"c":0.0,"d":2.0},
   "column1":{"a":3.0,"b":1,"c":0.0,"d":-1.0},
   "column2":{"a":4,"b":1,"c":5.0,"d":-1.0},
   "column3":{"a":3.0,"b":-1.0,"c":-1.0,"d":-1.0}
  }

print(type(udict))
print(udict)

result = np.array([[v[j] for j in ['a', 'b', 'c', 'd']] for k,v in udict.items()])
print(type(result))
print(result)

