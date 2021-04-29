import pandas as pd

pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)

values = pd.DataFrame({
'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],
'ord_date': ['2012-10-05','2012-09-10','2012-10-05','2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
'customer_id':[3002,3001,3001,3003,3002,3002,3001,3004,3003,3002,3003,3001],
'salesman_id':[5002,5003,5001,5003,5002,5001,5001,5003,5003,5002,5003,5001]})

print("values:")
print(values)
print()

result = values.groupby(['salesman_id', 'customer_id'])

for loop_index, loop_data in result:
    print(loop_index)
    print(loop_data)
print()

_n = 2
print("_n:")
print(_n)
print()

_indices_drop = values.groupby(['salesman_id', 'customer_id']).tail(_n).index
print("_indices_drop:")
print(_indices_drop)
print()

result_droprows = values.drop(_indices_drop, axis=0)
#   or
result_droprows = values.drop(_indices_drop)
print("result_droprows:")
print(result_droprows)

