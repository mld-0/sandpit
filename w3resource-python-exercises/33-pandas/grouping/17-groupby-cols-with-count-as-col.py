import pandas as pd

pd.set_option('display.max_rows', None)

values = pd.DataFrame({
'book_name':['Book1','Book2','Book3','Book4','Book1','Book2','Book3','Book5'],
'book_type':['Math','Physics','Computer','Science','Math','Physics','Computer','English'],
'book_id':[1,2,3,4,1,2,3,5]})

print("values:")
print(values)
print()

result = values.groupby(['book_name', 'book_type'])
print("result.groups:")
print(result.groups)
print()

result_count = result['book_type'].count().to_frame('count').reset_index()
#   or
result_count = result['book_type'].count().reset_index(name='count')
print("result_count:")
print(type(result_count))
print(result_count)
