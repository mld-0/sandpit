from collections import Counter

def remove_duplicates(values):
    values_counter = Counter(values)
    result = [x for x in values if values_counter[x] == 1]
    #   or
    result = [x for x in values if values.count(x) == 1]
    print(result)
    
remove_duplicates([1,2,3,2,3,4,5])
remove_duplicates([1,2,3,2,4,5])
remove_duplicates([1,2,3,4,5])
