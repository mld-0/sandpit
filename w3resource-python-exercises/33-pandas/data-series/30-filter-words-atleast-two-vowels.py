import pandas as pd
from collections import Counter

values = pd.Series(['Red', 'Green', 'Orange', 'Pink', 'Yellow', 'White', 'zzzz'])
print("values:")
print(values)

_count_vowels = lambda x: sum([Counter(x.lower()).get(c, 0) for c in list('aeiou')])

values_vowelcount = values.map(_count_vowels)
print("values_vowelcount:")
print(values_vowelcount.to_list())

_filter_atleast_two_vowels = lambda x: _count_vowels(x) >= 2

result_indices = values.map(_filter_atleast_two_vowels)
print("result_indices:")
print(result_indices.to_list())

result = values[result_indices]
print("result:")
print(result)

