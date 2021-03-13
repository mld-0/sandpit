import cProfile
def sum_vals():
    print(1 + 2)
cProfile.run('sum_vals()')
