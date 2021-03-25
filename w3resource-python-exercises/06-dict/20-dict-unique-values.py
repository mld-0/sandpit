
def dict_unique_values(L):
    result_set = set()
    for d in L:
        for k, v in d.items():
            result_set.update([v])
    #   or
    result_set = set([v for d in L for k, v in d.items()])
    print(result_set)

L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
dict_unique_values(L)

