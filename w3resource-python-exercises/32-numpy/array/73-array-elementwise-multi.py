import numpy as np

x = np.arange(12).reshape(3, 4)
print(x)
for a in np.nditer(x, op_flags=['readwrite']):
    #a[...] = 3 * a
    a[...] = 3 * a
print(x)
print()

#   ...  -  ellipsis 
#   The ellipsis (three dots) indicates "as many ':' as needed". (Its name for use in index-fiddling code is Ellipsis, and it's not numpy-specific.) This makes it easy to manipulate only one dimension of an array, letting numpy do array-wise operations over the "unwanted" dimensions.
#   In slice syntax to represent the full slice in remaining dimensions
#   In type hinting to indicate only part of a type(Callable[..., int] or Tuple[str, ...])

#   or

x = np.arange(12).reshape(3, 4)
print(x)
x = x * 3
print(x)
