import random

def shuffle_list(values):
    result = values[:]
    random.shuffle(result)
    print(result)

shuffle_list([7,8, 120, 25, 44, 20, 27])
shuffle_list(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'])
