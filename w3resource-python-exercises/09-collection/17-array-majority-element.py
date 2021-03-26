import collections

def array_majority_element(values):
    values_counter = collections.Counter(values)
    result = list(sorted(values_counter.items(), key=lambda x: x[1], reverse=True))[0][0]
    print(result)

values = [10,10,20,30,40,10,20,10]
array_majority_element(values)
