
def substrings_with_k_distinct_chars(_str, k):
    result_count = 0
    for start in range(0, len(_str)-k+1):
        for end in range(start+k, len(_str)+1):
            substr = _str[start:end]
            if len(set(substr)) == k:
                result_count += 1
    print(result_count)
     
substrings_with_k_distinct_chars("wolf", 4)
substrings_with_k_distinct_chars("prwsoeriusfk", 4)

