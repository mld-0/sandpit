
def lists_to_dict(keys, values):
    result = dict(zip(keys, values))
    print(result)

keys = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
values = [1, 2, 2, 3]
lists_to_dict(keys, values)
