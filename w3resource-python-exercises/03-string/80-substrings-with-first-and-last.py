
def substrings_with_first_and_last(_str):
    results = []
    for start in range(0, len(_str)):
        for end in range(start+1, len(_str)+1):
            substr = _str[start:end]
            #if substr[0] == _str[0] and substr[-1] == _str[-1]:
            if substr[0] == substr[-1]:
                results.append(substr)
    print(len(results))

substrings_with_first_and_last("abc")

