import functools
nums = [10, 20, 30,]
product = functools.reduce(lambda a, b: a*b, nums)
print(product)
