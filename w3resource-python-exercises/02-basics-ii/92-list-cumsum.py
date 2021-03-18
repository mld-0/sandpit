import numpy as np

def list_cumsum(values):
    _cumsum = list(np.cumsum(values))
    #   or
    _cumsum = [sum(values[:i+1]) for i in range(len(values))]
    print(_cumsum)
    
list_cumsum([10, 20, 30, 40, 50, 60, 7])
list_cumsum([1, 2, 3, 4, 5])
list_cumsum([0, 1, 2, 3, 4, 5])
