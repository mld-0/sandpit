import time
import numpy as np

SIZE = 200000 

list_a = range(SIZE)
list_b = range(SIZE)
array_a = np.arange(SIZE)
array_b = np.arange(SIZE)

_starttime_list = time.time()
list_result = [(x,y) for x,y in zip(list_a, list_b)]
#print(list_result[:3] + ["..."] + list_result[-3:])
_elapsedtime_list = time.time() - _starttime_list
print("combine lists")
print(_elapsedtime_list)

_starttime_array = time.time()
array_result = np.column_stack((array_a, array_b))
#print(array_result)
_elapsedtime_array = time.time() - _starttime_array 
print("combine arrays")
print(_elapsedtime_array)

_starttime_list = time.time()
list_result = [(x+y) for x,y in zip(list_a, list_b)]
#print(list_result[:5] + ["..."] + list_result[-5:])
_elapsedtime_list = time.time() - _starttime_list
print("sum lists")
print(_elapsedtime_list)

_starttime_array = time.time()
array_result = array_a + array_b
#print(array_result)
_elapsedtime_array = time.time() - _starttime_array 
print("sum arrays")
print(_elapsedtime_array)


