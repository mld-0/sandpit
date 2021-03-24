import itertools

def generate_all_sublists(values):
    result = []
    for i in range(0, len(values)+1):
        loop_combinations = itertools.combinations(values, i)
        result = list(itertools.chain(result, loop_combinations))
    print(result)

values = [10, 20, 30, 40]
generate_all_sublists(values)



