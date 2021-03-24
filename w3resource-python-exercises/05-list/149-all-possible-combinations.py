import itertools

def all_possible_combinations_itertools(values):
    result = []
    for i in range(len(values)+1):
        loop_result = list(itertools.combinations(values, i))
        result += loop_result
    print(result)

values = ['orange', 'red', 'green', 'blue']
all_possible_combinations_itertools(values)


