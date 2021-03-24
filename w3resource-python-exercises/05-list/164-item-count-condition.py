
def item_count_condition(values, f):
    results = [x for x in values if f(x)]
    print(len(results))

values = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
f = lambda x: x % 2 == 0 and x > 45

item_count_condition(values, f)
