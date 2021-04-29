import pandas as pd

values = pd.DataFrame( {'id' : ['A','A','A','A','A','A','B','B','B','B','B'], 
                    'type' : [1,1,1,1,2,2,1,1,1,2,2], 
                    'book' : ['Math','Math','English','Physics','Math','English','Physics','English','Physics','English','English']})

print("values:")
print(values)
print()

#   Get 'book' values for each id and type
result = values[['id', 'type', 'book']].drop_duplicates().groupby(['id', 'type'])['book'].apply(list).reset_index()
print("result:")
print(type(result))
print(result)
print()

#   Convert list of books to string
result['book'] = result['book'].apply(lambda x: ','.join(x))
print("result:")
print(result)

