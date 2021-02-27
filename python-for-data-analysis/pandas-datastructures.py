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

#       loc         only work on index
#       iloc        work on position
#       at          get scalar values. It's a very fast loc
#       iat         Get scalar values. It's a very fast iloc

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
print()

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
#       Calling reindex on this Series rearranges the data according to the new index, intro‐ ducing missing values if any index values were not already present
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj)
print(obj2)
print()

#   ffill   interpolation, forward fill values for new indexes
obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
print(obj3)
print(obj3.reindex(range(6), method='ffill'))
print()

#   reindex can alter either the (row) index, columns, or both.
frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'], columns=['Ohio', 'Texas', 'California'])
print(frame)
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print(frame2)
states = ['Texas', 'Utah', 'California']
print(frame.reindex(columns=states))
print()

#   reindex arguments
#       index           new sequence to use as index
#       method          interpolation (fill) method, 'ffill' fills forward, 'bfill' fills backwards
#       fill_value      substitute value to use for introduced missing data
#       limit           when forward or back filling, maximum size gap (number of elements) to fill
#       tolerance       when forward or back filling, maximum size gap for indexact matches
#       level           Match simple Index on level of MultiIndex; otherwise select subset of.
#       copy            If True, always copy underlying data even if new index is equivalant to old index, 
#                       if False, do not copy the data when the indexes are independent


#   Dropping Entries from an Axis
obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
print(obj.drop(['d', 'c']))
obj.drop('c', inplace=True)  # drop inplace

data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 'Colorado', 'Utah', 'New York'], columns=['one', 'two', 'three', 'four'])
#   remove rows
print(data.drop(['Colorado', 'Ohio']))  
#   remove columns
print(data.drop('two', axis=1))
#   or
print(data.drop(['two', 'four'], axis='columns'))
print()


#   Indexing, Selection, and Filtering
obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj[1])
print(obj[2:4])
print(obj[['b', 'a', 'd']])
print(obj[[1, 3]])
print(obj[obj < 2])
print(obj['b':'c'])  # slicing with labels is endpoint-inclusive
print()

obj['b':'c'] = 5  # assigns value to each item in corresponding series
print(obj)
print()

data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 'Colorado', 'Utah', 'New York'], columns=['one', 'two', 'three', 'four'])
#print(data)
print(data['two'])  # select column
print(data[['three', 'one']])  # columns
print(data[:2])  # select rows
print(data[data['three'] > 5])  # select rows

#   assignment using scalar-comparison indexing
data[data < 5] = 0
print(data)
print()

#   selection with loc and iloc
print(data.loc['Colorado', ['two', 'three']])
print(data.iloc[2, [3, 0, 1]])
print(data.iloc[2])  # select column
print(data.iloc[[1, 2], [3, 0, 1]])
print()

print(data.loc[:'Utah', 'two'])
print(data.iloc[:, :3][data.three > 5])
print()

#   Index operations with DataFrame
#       df[val]                     Select single column or sequence of columns, 
#                                   special cases: boolean array (filter rows), slice (slice rows), 
#                                   boolean DataFrame (set values per criterion)
#       df.loc[val]                 Select single row or subset of rows by label
#       df.loc[:, val]              Select single column or subset of columns by label
#       df.loc[val1, val2]          Select both row and column by label
#       df.iloc[where]              Select single row or subset of rows by integer position
#       df.iloc[:, where]           Select single column or subset of columns by integer position
#       df.iloc[where_i, where_j]   Select both rows and columns by integer position
#       df.at[label_i, label_j]     Select single scalar value by row and column label
#       df.iat[i, j]                Select single scalar valye by row and column positions (integers)
#       reindex()                   Select either rows or columns by labels
#       get_value(), set_value()    Select single valye by row and column label

#   Integer indexes
#       For consistent behaviour, use loc / iloc 
ser = pd.Series(np.arange(3.))
#>%     print(ser[-1])  # produces keyerror (potential ambiguity)
ser2 = pd.Series(np.arange(3.), index=['a', 'b', 'c'])
#>%     print(ser2[-1])  # does not produce keyerror


#   Arithmetic and Data Alignment
#       When you are adding together objects, if any index pairs are not the same, the respective index in the result will be the union of the index pairs - similar to an automatic outer join on the index labels.
#       The internal data alignment introduces missing values in the label locations that don’t overlap. Missing values will then propagate in further arithmetic computations.
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
print(s1 + s2)

#   In the case of DataFrame, alignment is performed on both the rows and the columns
#   Adding these together returns a DataFrame whose index and columns are the unions of the ones in each DataFrame
df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'), index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(df1 + df2)

#   If you add DataFrame objects with no column or row labels in common, the result will contain all nulls
df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'B': [3, 4]})
print(df1 + df2)

#   In arithmetic operations between differently indexed objects, you might want to fill with a special value, like 0, when an axis label is found in one object but not the other
df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
result = df1.add(df2, fill_value=0)
print(result)
result = df1.rdiv(1)  # equivelent to 1 / df1
print(result)
#   reindex also allows specifying of a fill value
print(df1.reindex(columns=df2.columns, fill_value=0))
print()

#   Flexible arithmetic methods (r<> methods have arguments flipped)
#       add, radd               addition (+)
#       sub, rsub               subtraction (-)
#       div, rdiv               division (/)
#       floordiv, rfloordiv     floor division (//)
#       mul, rmul               multiplication (*)
#       pow, rpow               exponentation (**)

#   Operations between DataFrame and Series
#       (With numpy) When we subtract arr[0] from arr, the subtraction is performed once for each row. This is referred to as broadcasting
arr = np.arange(12.).reshape((3, 4))
print(arr - arr[0])
#   Operations between a DataFrame and a Series are similar
#       arithmetic between DataFrame and Series matches the index of the Series on the DataFrame’s columns, broadcasting down the rows
frame = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.iloc[0]
print(frame - series)

#   If an index value is not found in either the DataFrame’s columns or the Series’s index, the objects will be reindexed to form the union
series2 = pd.Series(range(3), index=['b', 'e', 'f'])
print(frame + series2)

#   If you want to instead broadcast over the columns, matching on the rows, you have to use one of the arithmetic methods.
#   The axis number that you pass is the axis to match on. In this case we mean to match on the DataFrame’s row index (axis='index' or axis=0) and broadcast across
series3 = frame['d']
result = frame.sub(series3, axis='index')
print(result)
print()


#   Function Application and Mapping
#       NumPy ufuncs (element-wise array methods) also work with pandas objects
frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(np.abs(frame))

#   apply()     Apply a function along an axis of the DataFrame
f = lambda x: x.max() - x.min()
print(frame.apply(f))  # apply to each row
print(frame.apply(f, axis='columns'))  # apply to each column
#   The function passed to apply need not return a scalar value; it can also return a Series with multiple values
f = lambda x: pd.Series([x.min(), x.max()], index=['min', 'max'])
print(frame.apply(f))

#   applymap()  applies a function that accepts and returns a scalar to every element of a DataFrame
format = lambda x: '%.2f' % x
print(frame.applymap(format))
print()


#   Sorting and Ranking
obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
print(obj.sort_index())

#   sort_index()    With a DataFrame, you can sort by index on either axis 
frame = pd.DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'], columns=['d', 'a', 'b', 'c'])
print(frame.sort_index())  # sort by rows
print(frame.sort_index(axis=1))  # sort by columns
#   or
#>%     print(frame.sort_index(axis='columns'))
print(frame.sort_index(axis=1, ascending=False))  
print()

#   sort_values()   Sort a series by its values
obj = pd.Series([4, 7, -3, 2])
print(obj.sort_values())
#   Any missing values are sorted to the end of the Series by default
obj = pd.Series([4, np.nan, 7, np.nan, -3, 2])
print(obj.sort_values())

#   When sorting a DataFrame, you can use the data in one or more columns as the sort keys. To do so, pass one or more column names to the by option of sort_values
frame = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
print(frame.sort_values(by='b'))
print(frame.sort_values(by=['a', 'b']))  # pass a list of names to sort by multiple columns
print()

#   Ranking assigns ranks from one through the number of valid data points in an array.
#       by default rank breaks ties by assigning each group the mean rank
obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
print(obj.rank())
#   Ranks can also be assigned according to the order in which they’re observed in the data
print(obj.rank(method='first'))
print()

frame = pd.DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1], 'c': [-2, 5, 8, -2.5]})
print(frame.rank())
print(frame.rank(axis='columns'))
print()

#   Tie breaking methods with rank
#       average         Assign the average rank to each entry in the equal group (default)
#       min             Use min rank for the whole group
#       max             Use max rank for the whole group
#       first           Assign ranks in the order values appear in the data
#       dense           Like min, but ranks always incrase by 1 in between groups <?>


#   Axis Indexes with Duplicate Labels
obj = pd.Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
#   check the uniqueness of index labels
print(obj.index.is_unique)
#   Indexing a label with multiple entries returns a Series, while single entries return a scalar value - Output type from indexing can vary based on whether a label is repeated or not
print(obj['a'])
print(obj['c'])
#   The same logic extends to indexing rows in a DataFrame:
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'a', 'b', 'b', 'c'])
print(df.loc['b'])
print(df.loc['c'])
print()

#   Summarizing and Computing Descriptive Statistics
#       pandas objects are equipped with a set of common mathematical and statistical methods. Most of these fall into the category of reductions or summary statistics, methods that extract a single value (like the sum or mean) from a Series or a Series of values from the rows or columns of a DataFrame. Compared with the similar methods found on NumPy arrays, they have built-in handling for missing data.
df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]], index=['a', 'b', 'c', 'd'], columns=['one', 'two'])
#   NA values are excluded unless the entire slice (row or column in this case) is NA 
print(df)
print(df.sum())
print(df.sum(axis='columns'))
#   or
#print(df.sum(axis=1))
#   disable skipping of NA values with skipna=False
print(df.mean(axis='columns', skipna=False))
print(df.describe())
print()

obj = pd.Series(['a', 'a', 'b', 'c'] * 4)
print(obj)
print(obj.describe())
print()

#   Options for reduction methods
#       axis            Axis to reduce over, 0 for rows, 1 for columns
#       skipna          Exclude missing values (True by default)
#       level           Reduce grouped by level if the axis is hierarchically indexed (MultiIndex) <?>

#   Descriptive and summary statistics methods
#       count               Number of non NA values
#       describe            Set of summary statistics for series, or each DF column
#       min, max            Min and Max values
#       argmin, argmax      Index locations (ints) where max/min values occur
#       idxmin, idxmax      Index locations (labels) where max/min values occur
#       quantile            Compute sample quantile from 0 to 1
#       sum                 Sum of values
#       mean                Mean of values
#       median              Arithmetic median (50% quantile) of values
#       mad                 Mean absolute deviation from mean value
#       prod                Product of all values
#       var                 Sample variance of all values
#       std                 Sample standard deviation of all values
#       skew                Sample skewness (3rd moment) of all values
#       kurt                Sample kurtosis (4th moment) of all values
#       cumsum              Cumulative sum of values
#       cummin, cummax      Cumulative min or max of values
#       cumprod             Cumulative product of values
#       diff                Compute first arithmetic difference (useful for time series)
#       pct_change          Compute percentage change


#   Correlation and Covariance
import pandas_datareader.data as web
#   TODO: 2021-02-27T23:05:25AEDT save all_data, and if saved data is found, load from file instead of internet
all_data = {ticker: web.get_data_yahoo(ticker) for ticker in ['GOOG', 'AMD', 'INTC', 'TSM']}
price = pd.DataFrame({ticker: data['Adj Close'] for ticker, data in all_data.items()})
volume = pd.DataFrame({ticker: data['Volume'] for ticker, data in all_data.items()})
returns = price.pct_change()
print(returns)
#   correlation / covariance between columns
print(returns['TSM'].corr(returns['INTC']))
print(returns['TSM'].cov(returns['INTC']))
#   correlation matrix
correlation = returns.corr()
print(correlation)
#   covariance matrix
covariance = returns.cov()
print(covariance)
print()
print(returns.corrwith(volume))
print()


#   Unique Values, Value Counts, and Membership
obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
#   unique()    array of the unique values in a series, The Series is sorted by value in descending order as a convenience.
unqiues = obj.unique()
print(unqiues)
#   value_counts()  computes a series containing value frequencies
counts = pd.value_counts(obj.values, sort=False)
print(counts)
#   isin()      vectorized set membership check
#       useful in filtering a dataset down to a subset of values in a Series or column in a DataFrame
mask = obj.isin(['b', 'c'])
print(mask)
print(obj[mask])
#   Index.get_indexer()     Compute indexer and mask for new index given the current index. The indexer should be then used as an input to ndarray.take to align the current data to the new index.
to_match = pd.Series(['c', 'a', 'b', 'b', 'c', 'a'])
unique_vals = pd.Series(['c', 'b', 'a'])
indexer_values = pd.Index(unique_vals).get_indexer(to_match)
print(indexer_values)

#   Methods
#       isin            Boolean array indicating whether each Series value is contained in the passed sequence of values
#       match           Integer indicies for each value in an array into another array, helpful for data alignment
#       unique          Array of unique values in a series, (in order observed)
#       value_counts    Series containing unique values as its index and frequencies as its values

#   Histogram
data = pd.DataFrame({'Qu1': [1, 3, 4, 3, 4], 'Qu2': [2, 3, 1, 2, 3], 'Qu3': [1, 5, 2, 4, 4]})
result = data.apply(pd.value_counts).fillna(0)
print(result)



#   }}}1
