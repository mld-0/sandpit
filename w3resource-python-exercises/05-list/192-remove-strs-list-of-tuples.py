
def remove_strs_list_of_tuples(values):
    result = [tuple(x for x in T if not isinstance(x, str)) for T in values]
    print(result)

values = [(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]
remove_strs_list_of_tuples(values)
