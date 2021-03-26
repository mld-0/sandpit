from collections import Counter

def char_occurence_more_less_than(values, c):
    result_count = Counter()
    for x in values:
        result_count.update(x)

    result_count = dict(sorted(result_count.items(), key=lambda x: x[1], reverse=True))

    result_gt_c = [x[0] for x in result_count.items() if x[1] > c]
    result_lt_c = [x[0] for x in result_count.items() if x[1] < c]

    print(result_gt_c)
    print(result_lt_c)

values = ['abcd', 'iabhef', 'dsalsdf', 'sdfsas', 'jlkdfgd']
char_occurence_more_less_than(values, 3)
