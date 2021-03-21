
def count_substrings(_str):
    result_count = int(len(_str) * (len(_str) + 1) / 2)
    #   or
    result_count = 0
    for start in range(0, len(_str)):
        for end in range(start+1, len(_str)+1):
            substr = _str[start:end]
            result_count += 1
    print(result_count)

count_substrings("w3resource")
