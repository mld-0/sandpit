import numpy as np
import pandas as pd

pd.set_option('display.max_rows', None)

values = pd.DataFrame({
'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
'purch_amt':[150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
'ord_date': ['05-10-2012','09-10-2012','05-10-2012','08-17-2012','10-09-2012','07-27-2012','10-09-2012','10-10-2012','10-10-2012','06-17-2012','07-08-2012','04-25-2012'],
'customer_id':['C3001','C3001','D3005','D3001','C3005','D3001','C3005','D3001','D3005','C3001','D3005','D3005'],
'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]})

print("values:")
print(values)
print()

_start_C = lambda x: (x.str[0] == 'C').sum()

result = values.groupby('salesman_id').agg(\
    customer_id_start_C = ('customer_id', _start_C), 
    customer_id_list = ('customer_id', lambda x: ', '.join(x)),
    purchase_amt_gap = ('purch_amt', lambda x: x.max() - x.min())
    )

print("result:")
print(result)
