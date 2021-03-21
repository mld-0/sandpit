import difflib

def longest_common_substring(a, b):
    seqmatch = difflib.SequenceMatcher(None, a, b)
    match = seqmatch.find_longest_match(0, len(a), 0, len(b))

    if match.size == 0:
        print(None)
        return
    
    result = a[match.a:match.a+match.size]
    print(result)

longest_common_substring("abcdefgh", "xswerabcdwd")
