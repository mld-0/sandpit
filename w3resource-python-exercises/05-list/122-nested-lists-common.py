
def nested_lists_common(values):
    encountered = set()
    result = set()
    for x in values:
        for y in x:
            if y in encountered:
                result.add(y)
            encountered.add(y)
    #   or
    result = set.intersection(*map(set, values))
    print(result)


values = [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
nested_lists_common(values)
