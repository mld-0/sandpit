import pandas as pd

#   Options for closed: [left, right, both, neither]

df_interval = pd.DataFrame({"X":[1, 2, 3, 4, 5, 6, 7]},
                            index = pd.IntervalIndex.from_breaks(
                            [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3, 3.5], closed='neither'))    
print("Create an Interval Index using IntervalIndex.from_breaks:")
print(df_interval)
print(df_interval.index)

df_interval = pd.DataFrame({"X":[1, 2, 3, 4, 5, 6, 7]},             
                            index = pd.IntervalIndex.from_tuples(
                            [(0, .5), (.5, 1), (1, 1.5), (1.5, 2), (2, 2.5), (2.5, 3), (3, 3.5)], closed='right'))
print("Create an Interval Index using IntervalIndex.from_tuples:")
print(df_interval)
print(df_interval.index)

df_interval = pd.DataFrame({"X":[1, 2, 3, 4, 5, 6, 7]},             
                            index = pd.IntervalIndex.from_arrays(
                            [0, .5, 1, 1.5, 2, 2.5, 3], [.5, 1, 1.5, 2, 2.5, 3, 3.5], closed='both'))
print("Create an Interval Index using IntervalIndex.from_arrays:")
print(df_interval)
print(df_interval.index) 

