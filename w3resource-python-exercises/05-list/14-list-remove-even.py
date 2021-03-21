
def list_remove_even(values):
    result = []
    for n in values:
        if not n % 2 == 0:
            result.append(n)
    print(result)

list_remove_even([7,8, 120, 25, 44, 20, 27])
