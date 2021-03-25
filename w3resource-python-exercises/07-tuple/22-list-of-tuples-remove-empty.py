
def list_of_tuples_remove_empty(t):
    result = [x for x in t if len(x) >= 1]
    print(result)

t = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
list_of_tuples_remove_empty(t)
