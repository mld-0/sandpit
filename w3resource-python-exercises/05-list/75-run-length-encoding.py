import itertools

def run_length_encoding(values):
    if isinstance(values, str):
        values = [x for x in values]
    result = [[len(list(g)), k] for k, g in itertools.groupby(values)]
    print(result)


values = [1, 1, 2, 3, 4, 4.3, 5, 1]
run_length_encoding(values)

values = 'automatically'
run_length_encoding(values)

