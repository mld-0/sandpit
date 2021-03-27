import functools

fib = lambda n: functools.reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0,1])

print(fib(9))
