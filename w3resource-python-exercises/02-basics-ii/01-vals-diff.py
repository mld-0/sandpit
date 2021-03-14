def are_unique(values):
    if len(set(values)) != len(values):
        print(False)
    else:
        print(True)

vals_1 = [1,5,7,9]
vals_2 = [2,4,5,5,7,9]

are_unique(vals_1)
are_unique(vals_2)
