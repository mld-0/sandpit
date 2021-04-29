import numpy as np
import pandas as pd

pd.set_option('display.max_rows', None)

values = pd.DataFrame({
'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],
'ord_date': ['05-10-2012','09-10-2012','05-10-2012','08-17-2012','10-09-2012','07-27-2012','10-09-2012','10-10-2012','10-10-2012','06-17-2012','07-08-2012','04-25-2012'],
'customer_id':[3001,3001,3005,3001,3005,3001,3005,3001,3005,3001,3005,3005],
'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]})

values['ord_date'] = pd.to_datetime(values['ord_date'])

print("values:")
print(values)
print()

#   Without using ord_date as index
result = values.groupby(pd.Grouper(freq='M', key='ord_date')).agg({'purch_amt': np.sum})
print("result:")
print(type(result))
print(result)
print()

#   Using ord_date as index
result = values.set_index('ord_date').groupby(pd.Grouper(freq='M')).agg({'purch_amt': np.sum})
print("result:")
print(type(result))
print(result)
