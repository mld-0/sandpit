
def nest_lists_every_nth(values, n):
    result = [[values[i+j*n] for j in range(len(values)//n+1) if i+j*n < len(values)] for i in range(n)]
    #   or
    result = [values[i::n] for i in range(n)]
    print(result)

values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
nest_lists_every_nth(values, 3)

values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
nest_lists_every_nth(values, 3)

values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
nest_lists_every_nth(values, 3)



