from collections import defaultdict

def max_aggregate_from_tuples(values):
    values_aggregate = defaultdict(int)
    for d in values:
        k, v = d[0], d[1]
        values_aggregate[k] += v

    values_aggregate = list(values_aggregate.items())
    values_aggregate_sorted = sorted(values_aggregate, key=lambda x: x[1], reverse=True)

    print(values_aggregate_sorted[0])

values = [('Juan Whelan', 90), ('Sabah Colley', 88), ('Peter Nichols', 7), ('Juan Whelan', 122), ('Sabah Colley', 84)]
max_aggregate_from_tuples(values)

