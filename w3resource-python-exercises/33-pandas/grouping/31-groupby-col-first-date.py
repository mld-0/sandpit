import numpy as np
import pandas as pd

pd.set_option('display.max_rows', None)

values = pd.DataFrame({
'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],
'ord_date': ['2012-10-05','2012-09-10','2012-10-05','2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
'customer_id':[3005,3001,3002,3009,3005,3007,3002,3004,3009,3008,3003,3002],
'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5004,5003,5002,5004,5001]})

values['ord_date'] = pd.to_datetime(values['ord_date'])

print("values:")
print(values)
print()

result = values.groupby('salesman_id')['ord_date'].min()
#   or
result = values.groupby('salesman_id')['ord_date'].apply(np.min)
print("result:")
print(result)
print()

result = values.groupby('salesman_id').agg({'ord_date': (('ord_date_count', 'count'), ('ord_date_min', np.min), ('ord_date_max', np.max))})
print("result:")
print(result)

