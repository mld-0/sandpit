
def digit_distance(a, b):
    a_str = str(a)[::-1]
    b_str = str(b)[::-1]
    result = 0
    for loop_a, loop_b in zip(a_str, b_str):
        result += abs(int(loop_a) - int(loop_b))
    print(result)

digit_distance(123, 256)
digit_distance(23, 56)
digit_distance(1, 2)
digit_distance(24232, 45645)

