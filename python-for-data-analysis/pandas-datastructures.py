#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
import pandas as pd
import numpy as np
#   {{{2
#   See: OReilly Python for Data Analysis Ch5

#   Series:
#   A Series is a one-dimensional array-like object containing a sequence of values (of similar types to NumPy types) and an associated array of data labels, called its index.
#   The simplest Series is formed from only an array of data
#       Since we did not specify an index for the data, a default one consisting of the integers 0 through N - 1 (where N is the length of the data) is created
obj = pd.Series([4, 7, -5, 3])
print(obj)
print(obj.values)  # Data array
print(obj.index)  # like range(4)
print()

#   A series index can be altered by in-place assignment
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)
print()

#   Often it will be desirable to create a Series with an index identifying each data point with a label
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
print(type(obj2.index))
print(obj2.index)
print()

#   Accessing element by index
print(obj2['a'])
print(obj2['b'])
print(obj2[ ['c', 'a', 'd'] ])
print()

#   Using NumPy functions or NumPy-like operations, such as filtering with a boolean array, scalar multiplication, or applying math functions, will preserve the index-value link

#   Another way to think about a Series is as a fixed-length, ordered dict, as it is a map‐ ping of index values to data values. 
#   It can be used in many contexts where you might use a dict:
print('b' in obj2)
print('b' in obj2.index)
print(4 in obj2)
print(4 in obj2.values)
print()

#   Create Series from dict
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
print(obj3)

#   Specifying keys
#      Here, three values found in sdata were placed in the appropriate locations, but since no value for 'California' was found, it appears as NaN (not a number), which is con‐ sidered in pandas to mark missing or NA values. Since 'Utah' was not included in states, it is excluded from the resulting object. 
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
print(obj4)
print()

#   Detecting missing data
print(pd.isnull(obj4))
print(pd.notnull(obj4))
print(obj4.isnull())
print()

print(obj3 + obj4)
print()

#   Both the Series object itself and its index have a name attribute, which integrates with other key areas of pandas functionality
obj4.name = 'population'
obj4.index.name = 'state'
print(obj4)
print()


#   DataFrame:
#       A DataFrame represents a rectangular table of data and contains an ordered collec‐ tion of columns, each of which can be a different value type (numeric, string, boolean, etc.).
#       The DataFrame has both a row and column index; it can be thought of as a dict of Series all sharing the same index.

#   There are many ways to construct a DataFrame, though one of the most common is from a dict of equal-length lists or NumPy arrays
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'], 'year': [2000, 2001, 2002, 2001, 2002, 2003], 'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print(frame)
print()

#   For large DataFrames, the head method selects only the first five rows
print(frame.head())
print()

#   If you specify a sequence of columns, the DataFrame’s columns will be arranged in that order
frame = pd.DataFrame(data, columns=['year', 'state', 'pop'])
print(frame)
print()

#   If you pass a column that isn’t contained in the dict, it will appear with missing values in the result
#       (however, len(index) must match length of data)
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five', 'six'])
print(frame2)
print()

#   Columns in a DataFrame can be retrieved as a Series, either by dict-like notation, or by attribute
#       Note that the returned Series have the same index as the DataFrame, and their name attribute has been appropriately set
series_states = frame2['state']
#   or
series_states = frame2.state
print(series_states)
print()

#   Rows can be retrieved by position or name with the special 'loc' attribute
print(frame2.loc['three'])
print()

#   Columns can be modified by assignment. For example, the empty 'debt' column could be assigned a scalar value or an array of values
frame2['debt'] = 16.5
print(frame2)
frame2['debt'] = np.arange(6.0)
print(frame2)
print()

#   When you are assigning lists or arrays to a column, the value’s length must match the length of the DataFrame
#   If you assign a Series, its labels will be realigned exactly to the DataFrame’s index, inserting missing values in any holes
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
print(frame2)
print()

#   add a new column of boolean values where the state column equals 'Ohio' (column to be deleted next)
frame2['eastern'] = frame2.state == 'Ohio'
del frame2['eastern']

#   Another common form of data is a nested dict of dicts
pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
#   Set index and column name attribute
frame3.index.name = 'year'; frame3.columns.name = 'state'
print(frame3)
#   Transpose (swap rows and columns)
print(frame3.T)
#   numpy array of data values
print(frame3.values)
print()

#   Continue: 2021-02-23T23:27:04AEDT Python for Data Analysis Ch 5

#   Possible data inputs to DataFrame constructor
#       2d ndarray                                  Matrix of data 
#       dict of arrays, lists, or tuples            Each sequence becomes a column in the DataFrame, must all be same length
#       Numpy structured/record array               Treated as the 'dict-of-arrays' case
#       dict of Series                              Each value becomes a column, indexes from each Series are unioned together 
#                                                   to form the index if no explict index is passed
#       dict of dicts                               Each inner dict becomes a column, keys are unioned to form the row index
#       List of dicts or Series                     Each item becomes a row in the DataFrame, union of dict keys or series indexes
#                                                   becomes the DataFrame's column labels
#       list of list or tuples                      Treated as the 2d ndarray case
#       Another DataFrame                           DataFrame's indexes are used unless different ones are passed
#       NumPy MaskedArray                           Like the 2d ndarray case, except masked values become NA/missing in the result


#   Index Objects:
#       Pandas's Index objects are responsible for holding the axis labels and other metadata (like the axis name or names). Any array or other sequence of labels you use when constructing a Series or DataFrame is internally converted to an Index
#       Index objects are immutable
obj = pd.Series(range(3), index=['a', 'b', 'c'])
index = obj.index
print(index)

#   In addition to being array-like, an Index also behaves like a fixed-size set. Unlike Python sets, a pandas Index can contain duplicate labels
print(frame3.columns)
print('Ohio' in frame3.columns)
print(2003 in frame3.index)

#   Index methods and properties
#       append                  Concatenate with additional Index objects, producing a new Index 
#       difference              Compute set difference as an Index
#       intersection            Compute set intersection
#       union                   Compute set union
#       isin                    Compute boolean array indicating whether each value is contained in the passed collection 
#       delete                  Compute new Index with element at index i deleted
#       drop                    Compute new Index by deleting passed values
#       insert                  Compute new Index by inserting element at index i
#       is_monotonic            Returns True if each element is greater than or equal to the previous element 
#       is_unique               Returns True if the Index has no duplicate values
#       unique                  Compute the array of unique values in the Index

#   Reindexing

#   Dropping Entries from an Axis

#   Indexing, Selection, and Filtering

#   Arithmetic and Data Alignment

#   Function Application and Mapping

#   Sorting and Ranking

#   Axis Indexes with Duplicate Labels

#   Summarizing and Computing Descriptive Statistics
#   Correlation and Covariance
#   Unique Values, Value Counts, and Membership



#   }}}1
