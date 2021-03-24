
def index_of_nones(values):
    result = [i for i in range(len(values)) if values[i] is None]
    print(result)

values = [1, None, 5, 4, None, 0, None, None]
index_of_nones(values)

