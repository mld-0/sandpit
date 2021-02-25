import numpy as np

#   See: OReilly Python for Data Analysis Ch4

#   Create 2x3 (rows x cols) random np array
data = np.random.rand(2, 3)

#   Multiply all elements by 10
result = data * 10
print(f"result:\n{result}")

#   Add elements in each corresponding cell
result = data + data
print(f"result:\n{result}")

#   Shape and type of array
print(data.shape)
print(data.dtype)
print()

#   Create python list of numbers, and convert to np array
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
print(f"arr1:\n{arr1}")
print(f"arr1.ndim=({arr1.ndim})")
print(f"arr1.shape=({arr1.shape})")
print(f"arr1.dtype=({arr1.dtype})")
print()

#   Nested sequences, like a list of equal-length lists, will be converted into a multidimen‐ sional array
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print(f"arr2:\n{arr2}")
print(f"arr2.ndim=({arr2.ndim})")
print(f"arr2.shape=({arr2.shape})")
print(f"arr2.dtype=({arr2.dtype})")
print()

#   zeros and ones create arrays of 0s or 1s, respectively, with a given length or shape
print(np.zeros(10))
print(np.zeros((3,6)))
print()

#   higher dimension arrays are created with a tuple for the shape
print(np.zeros((2,3,2)))  
print()

#   arange() is the array-valued version of the python range() function
print(np.arange(15))
print()

#   Array creation functions
#       array           Convert input data to an ndarray either by inferring or explicitly specifying a dtype; copies the input data by default
#       asarray         Convert input to ndarray, but do not copy if input is already an ndarray
#       arange          As per range(), but return an ndarray instead of list
#       zeros           Produce array of all-0s with a given shape (and dtype)
#       ones            Produce array of all-1s with a given shape (and dtype)
#       zeros_like      Produce array of all-0s with same shape and type as array argument
#       ones_like       Produce array of all-1s with same shape and type as array argument
#       full            Produce array of given shape (and dtype), with all values set to 'fill' value
#       full_like       Produce array with same shape (and type) as array argument, with all values set to 'fill' value
#       eye, identity   Produce a square n x n matrix (1s on diagonal, 0s elsewhere)

#   Numpy data types (with shorthand type-codes)
#       int8, uint8 int16, uint16 int32, uint32 int64, uint64  (i1, u1, i2, u2, i4, u4, i8, u8)
#       float16 float32 float64 float128  (f2, f4/f, f8/d)
#       complex64, complex128, complex256  (c8, c16, c32, n/a)
#       bool  (?)
#       object  (O)
#       string_  (S)
#       unicode_  (U)

#   Convert array dtype
#       converting floats to integers will truncate decimal component
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = arr1.astype(np.float64)
print(f"arr1.dtype({arr1.dtype})")
print(f"arr2.dtype({arr2.dtype})")
print()

#   convert numbers-as-strings to floats
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
numeric_floats = numeric_strings.astype(float)



#   arithmetic operators with scalars propogate the scalar argument to each element in the array
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(1 / arr)
print(arr ** 0.5)
print()

#   Comparisons between arrays of the same size yield boolean arrays
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
print(arr2 > arr)
print()


#   basic indexing and slicing
#       a one-dimensional array behaves similarly to a python list
#       assigning a scalar to a slice propogates (assigns) the value to the entire section
#       (unlike python arrays), slices are views (not copies) to the origional array
#           To explicitly copy the array (slice), use 'arr[5:8].copy()'
arr = np.arange(10)
print(arr[5:8])
arr[5:8] = 12
print(arr)
print()

#   In a two-dimensional array, the elements at each index are  one-dimensional arrays (instead of scalars)
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"arr2d=({arr2d})")
print(f"arr2d[2]=({arr2d[2]})")
#   equivelent
print(f"arr2d[0][2]=({arr2d[0][2]})")
print(f"arr2d[0,2]=({arr2d[0,2]})")
print()

#   equivelent
print(f"arr2d[:2]=({arr2d[:2]})")
print(f"arr2d[:2 , :]=({arr2d[:2 , :]})")
print()


#   In multidimensional arrays, if you omit later indices, the returned object will be a lower dimensional ndarray consisting of all the data along the higher dimensions.
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
#print(f"arr3d=({arr3d})")
print(f"arr3d[0]=({arr3d[0]})")

#   both scalars and arrays can be assigned to this slice arr3d[0]
arr3d_oldvalues = arr3d[0].copy()
arr3d[0] = 42
print(f"arr3d[0]=({arr3d[0]})")
arr3d[0] = arr3d_oldvalues
print(f"arr3d[0]=({arr3d[0]})")
print()


#   Boolean indexing
#       Boolean selection will not fail if the boolean array is not the correct length, so I recommend care when using this feature.
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)
print(f"names=({names})")
print(f"data=({data})")

print(names == "Bob")
#   Filter rows by names == Bob
print(data[names == "Bob"])
#   Restrict to cols >= 2
print(data[names == "Bob", 2:])

#   Equivelent
#>%     data[names != 'Bob']
#>%     data[~(names == 'Bob')]

#   Combining boolean conditions
#       The Python keywords and and or do not work with boolean arrays. Use & (and) and | (or) instead.
mask = (names == 'Bob') | (names == 'Will')
print(data[mask])

#   Set all -ive values in data to 0
data[data < 0] = 0
print(data)
print()

#   Fancy indexing
#       indexing using integer arrays
#        fancy indexing, unlike slicing, always copies the data into a new array.
arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i
print(arr)

#   Select rows in a particular order
print(arr[[4, 3, 0, 6]])
print(arr[[-3, -5, -7]])

arr = np.arange(32).reshape((8, 4))
#   passing multiple index array selects a one-dimensional array of elements corresponding to each tuple of indices
#       regardless of the dimension of the array, the result of fancy indexing i always one-dimenional
print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])  # Here the elements (1, 0), (5, 3), (7, 1), and (2, 2) are selected

#   getting a rectangular region formed by given rows and columsn
print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])
print()

#   Transposing arrays and swapping axis
#       Transposing is a special form of reshaping that similarly returns a view on the underlying data without copying anything. 
#       Arrays have the transpose method and also the special T attribute
arr = np.arange(15).reshape((3, 5))
print(arr)
print(arr.T)
print()

#   For higher dimensional arrays, transpose will accept a tuple of axis numbers to per‐ mute the axes
arr = np.arange(16).reshape((2, 2, 4))
print(arr)
print(arr.transpose(1, 0, 2))  # Here, the axes have been reordered with the second axis first, the first axis second, and the last axis unchanged

#   np.swapaxes()  takes a pair of axis numbers and switches the indicated axes to rear‐ range the data:
print(arr.swapaxes(1, 2))
print()


#   Universal functions (ufunc)
#       fast element-wise array functions
arr = np.arange(10)
print(np.sqrt(arr))
print(np.exp(arr))

#   Others, such as add or maximum, take two arrays (thus, binary ufuncs) and return a single array as the result
x = np.random.randn(8)
y = np.random.randn(8)
print(np.maximum(x, y))
print()

#   While not common, a ufunc can return multiple arrays. modf is one example, a vec‐ torized version of the built-in Python divmod; it returns the fractional and integral parts of a floating-point array
arr = np.random.randn(7) * 5
remainder, whole_part = np.modf(arr)
print(remainder)
print(whole_part)
print()

#   Unary ufuncs
#       abs, fabs sqrt square exp
#       log, log10, log2, log1p
#       sign ceil
#       floor
#       rint
#       modf
#       isnan isfinite, isinf
#       cos, cosh, sin, sinh, tan, tanh
#       arccos, arccosh, arcsin, arcsinh, arctan, arctanh
#       logical_not

#   Binary ufuncs
#       add
#       subtract
#       multiply
#       divide, floor_divide power
#       maximum, fmax minimum, fmin
#       mod
#       copysign
#       greater, greater_equal, less, less_equal, equal, not_equal
#       logical_and, logical_or, logical_xor


#   Vectorization
#   Example: Evaluate x^2 + y^2 over a rectanguar grid
#   np.meshgrid(x, y)
#       take two 1d arrays, and produce two 2d matricies corresponding to app pairs (x, y) in the two arrays
points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)
z = np.sqrt(xs ** 2 + ys ** 2)
print(z)
#import matplotlib.pyplot as plt
#plt.imshow(z, cmap=plt.cm.gray); 
#plt.colorbar()
#plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
print()


#   Conditional logic as array operators
#       np.where()
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
#   list comprehension implementation
result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
#   vector implemenation
result = np.where(cond, xarr, yarr)
print(result)
print()

#   suppose you had a matrix of randomly generated data and you wanted to replace all positive values with 2 and all negative values with –2
arr = np.random.randn(4, 4)
result = np.where(arr > 0, 2, -2)
print(result)
#   replace only positive values
result = np.where(arr > 0, 2, arr)
print(result)
print()


#   Statistical Models
#       sum(), mean(), std()
arr = np.random.randn(5, 4)
print(f"mean=({arr.mean()})")
# or
#   print(f"mean=({np.mean(arr)})")
print(f"sum=({arr.sum()})")

#   mean and sum take an optional axis argument
#        arr.mean(1) means “compute mean across the columns” where arr.sum(0) means “compute sum down the rows.
print(f"mean(axis=1)=({arr.mean(axis=1)})")
print(f"sum(axis=0)=({arr.mean(axis=0)})")

#   Other methods like cumsum and cumprod do not aggregate, instead producing an array of the intermediate results
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
print(arr.cumsum())
print(arr.cumprod())

arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(arr.cumsum(axis=0))
print(arr.cumprod(axis=1))
print()

#   Methods for boolean arrays
arr = np.random.randn(100)
#   Boolean values are coerced to 1 (True) and 0 (False) in the preceding methods. Thus, sum is often used as a means of counting True values in a boolean array
num_positive = (arr > 0).sum()
print(f"num_positive=({num_positive})")
print()

#   
bools = np.array([False, False, True, False])
print(bools)
print(f"any=({bools.any()})")
print(f"all=({bools.all()})")
print()

#   Like Python’s built-in list type, NumPy arrays can be sorted in-place with the sort method
arr = np.random.randn(6)
print(arr)
arr.sort()
print(arr)
print()

#   You can sort each one-dimensional section of values in a multidimensional array in- place along an axis by passing the axis number to sort
arr = np.random.randn(5, 3)
print(arr)
arr.sort(1)
print(arr)
print()

#   The top-level method np.sort returns a sorted copy of an array instead of modifying the array in-place. A quick-and-dirty way to compute the quantiles of an array is to sort it and select the value at a particular rank
large_arr = np.random.randn(1000)
large_arr.sort()
print(large_arr[int(0.05 * len(large_arr))])  # 5% quantile
print()


#   Unique and other Set logic
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(np.unique(names))
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
print(np.unique(ints))
print()

#   np.in1d()
values = np.array([6, 0, 0, 3, 2, 5, 6])
print(np.in1d(values, [2, 3, 6]))
print()

#   Array set operations
#       unique(x)           Sorted, unique elements in x
#       intersect1d(x, y)   Sorted, common elements in x and y
#       union1d(x, y)       Sorted union of elements in x and y
#       in1d(x, y)          Boolean array, whether element of x is in y
#       setdiff1d(x, y)     Set difference, elements in x not in y
#       setxor1d(x, y)      Set symmetric difference, elements that are in either array, but not both


#   File input and ouput with arrays
#       NumPy is able to save and load data to and from disk either in text or binary format.
#       Arrays are saved by default in an uncompressed raw binary format with file extension .npy If the file path does not already end in .npy, the extension will be appended.
#       np.save()
#       np.load()

#>%     arr = np.arange(10)
#>%     np.save('filename.npy', arr)
#>%     arr_load = np.load('filename.npy')

#   Saving multiple arrays:
#>%     np.savez('array_archive.npz', a=arr, b=arr)
#>%     arch = np.load('array_archive.npz')
#>%     b = arch['b']
#>%     a = arch['a']

#   np.savez_compressed()       Save data in compressed format
#>%     np.savez_compressed('arrays_compressed.npz', a=arr, b=arr)


#   Linear Algebra
#       Linear algebra, like matrix multiplication, decompositions, determinants, and other square matrix math, is an important part of any array library.
#       (Unlike matlab) * i an element-wise product intead of a dot product
x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])

z = x.dot(y)
#   or
z = np.dot(x, y)
print(z)

#   @   (python3.5+) infix operator, performs matrix multiplication
print(x @ y)
print(x @ np.ones(3))
print()

#   Inverse
import numpy.linalg
X = np.random.randn(5, 5)
mat = X.T.dot(X)
print(numpy.linalg.inv(mat))
print(mat.dot(numpy.linalg.inv(mat)))
print()

q, r = numpy.linalg.qr(mat)
#print(mat)
print(q)
print(r)
#print(q.dot(r))
print()

#   Common numpy.linalg functions
#       diag        Return diagonal elements of a square matrix as a 1d array, 
#                   or, convert a 1d array into a square matrix with zeros on the off-diagonal
#       dot         Matrix multiplication
#       trace       Compute the sum of diagonal elements
#       det         Compute the matrix determinant
#       eig         Compute the eigenvalues and eigenvectors of a square matrix
#       inv         Compuare the inverse of a square matrix
#       pinv        Compute the Moore-Penrose pseudo-inverse of a matrix
#       qr          Compute the QR decomosition
#       svd         Compute the singular value decomposition
#       solve       Solve the linear system AX=b for x, where A is a square matrix
#       lstsq       Compute the least-squares solution to Ax=b

#   Pseudorandom-number generation
#       numpy.random module supplements the built-in Python random with functions for efficiently generating whole arrays of sample values from many kinds of probabil‐ ity distributions
#       numpy.random is well over an order of magnitude faster for generating very large samples
#   Set numpy seed
#np.random.seed(1234)
samples = np.random.normal(size=(4, 4))

#   The data generation functions in numpy.random use a global random seed. To avoid global state, you can use numpy.random.RandomState to create a random number generator isolated from others
rng = np.random.RandomState(1234)
rng.randn(10)


#   Common numpy.random functions
#       seed            Seed random number generator
#       permutation     Return a random perumutation of a sequence, or a permuted range 
#       shuffle         Randomly permute a sequence in-place
#       rand            Draw samples from random distribution
#       randint         Draw random integers given a low-high range
#       randn           Draw samples from a normal distribution (mean=0, std=1) (matlab like)
#       binomial        Draw samples from a binomial distribution
#       normal          Draw samples from a normal (Gaussian) distribution
#       beta            Draw samples from a beta distrubtion
#       chisquare       Draw samples from a chi-square distribution
#       gamma           Draw samples from a gamma distribution
#       uniform         Draw samples from a uniform [0, 1) distribution


#   Random walks
#   pure python implementation
import random
position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)

#   numpy implementation
nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()

#   statistics:
print(f"walk.min()=({walk.min()})")
print(f"walk.max()=({walk.max()})")

#   first crossing time
#       time at which the random walk reacheds a particular distance (abs(10)) from origin
fct = (np.abs(walk) >= 10).argmax()
print(f"fct=({fct})")
print()

#   Simulating multiple random walks
nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps))
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)
print(f"walks.max()=({walks.max()})")
print(f"walks.min()=({walks.min()})")

#   minimum crossing time to 30 or -30 for our multiple walks
hits30 = (np.abs(walks) >= 30).any(1)
print(f"hits30.sum()=({hits30.sum()})")
crossing_times = (np.abs(walks[hits30]) >= 30).argmax(1)
print(f"crossing_times.mean()=({crossing_times.mean()})")
print()

