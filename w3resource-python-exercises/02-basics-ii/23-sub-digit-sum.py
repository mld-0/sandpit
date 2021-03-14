def sub_digit_sum(num):
    count = 0
    while (num > 0):
        num_digits = [int(x) for x in str(num)]
        digits_sum = sum(num_digits)
        num = num - digits_sum
        count += 1
    print(count)

sub_digit_sum(9)
sub_digit_sum(21)
