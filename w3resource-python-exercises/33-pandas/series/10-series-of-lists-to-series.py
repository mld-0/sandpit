import pandas as pd

values = pd.Series([ ['Red', 'Green', 'White'], ['Red', 'Black'], ['Yellow']])
print(type(values))
print(values)
print()

result_df = values.apply(pd.Series)
print(type(result_df))
print(result_df)
print()

result_df_stack = result_df.stack()
print(type(result_df_stack))
print(result_df_stack)
print()



