import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)

values = pd.DataFrame({
'ord_no':[np.nan,np.nan,70002,70004,np.nan,70005,np.nan,70010,70003,70012,np.nan,70013],
'purch_amt':[np.nan,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],
'ord_date': [np.nan,'2012-09-10',np.nan,'2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
'customer_id':[np.nan,3001,3001,3003,3002,3001,3001,3004,3003,3002,3001,3001]})

print("values:")
print(values)
print()

result = values.dropna(how='all')
result = values[~values.isna().all(axis=1)]

print("result:")
print(result)
