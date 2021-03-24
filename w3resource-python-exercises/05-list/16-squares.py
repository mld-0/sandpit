
def gen_squares(n):
    result = [i**2 for i in range(1, n+1)]
    return result

result = gen_squares(30)
print(result[:5], result[-5:])
