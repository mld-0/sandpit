import itertools

def carry_number(a, b):
    #print("%s, %s" % (a, b))
    a_str = str(a)
    b_str = str(b)
    total_sum = 0
    carry_count = 0
    for i, (digit_a, digit_b) in enumerate(itertools.zip_longest(a_str, b_str)):
        #print("%s + %s, x%s" % (digit_a, digit_b, i))
        loop_sum = int(digit_a) + int(digit_b)
        carry_count += 1 if loop_sum > 10 else 0
        total_sum += loop_sum * 10 ** i
    print("%s, %s" % (total_sum, carry_count))

carry_number(786, 457)
carry_number(5, 6)
