import functools
import operator

def dict_multi_items(d):
    result = functools.reduce(operator.mul, d.values())
    #   or
    result = 1
    for x in d.values():
        result *= x
    print(result)

my_dict = {'data1':100,'data2':-54,'data3':247}
dict_multi_items(my_dict)
