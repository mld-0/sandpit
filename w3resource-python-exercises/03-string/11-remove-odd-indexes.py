
def remove_odd_indexes(_str):
    result = ''.join([_str[i] for i in range(len(_str)) if i % 2 == 0])
    print(result)

remove_odd_indexes('abcdef')
remove_odd_indexes('python')
