import random

def range_except_vals(a, b, _except):
    results = [i for i in range(a, b) if not i in _except]
    return results

def range_choice_except_vals(a, b, _except):
    choices = range_except_vals(a, b, _except)
    result = random.choice(choices)
    print(result)

range_choice_except_vals(1, 10, [2,9,10])
range_choice_except_vals(-5, 5, [-5,0,4,3,2])
