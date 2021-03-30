import numpy as np

data = [[1,2,3,4], ['Red', 'Green', 'White', 'Orange'], [12.20,15,20,40]]
print(data)

result_records = np.core.records.fromarrays(data, names='a,b,c')
print(result_records)

