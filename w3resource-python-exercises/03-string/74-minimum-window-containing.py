from collections import Counter

def contains_chars_of(a, b):
    """Does a contain all the characters of b?"""
    a_count = Counter(a)
    b_count = Counter(b)
    b_chars = set(b)
    for c in b_chars:
        if not c in a or b_count[c] < a_count[a]:
            return False
    return True

#   More efficent method than brute-force?
def minimum_window_containing(a, b):
    """Find the shortest substring(s) in a which contain all the characters in b."""
    if not contains_chars_of(a, b):
        print(None)
        return
    result_windows = []
    result = a
    min_length = len(b)
    max_length = len(a)
    for window_start in range(0, max_length-min_length):
        for window_end in range(window_start+min_length, max_length):
            window = a[window_start:window_end]
            if contains_chars_of(window, b):
                result_windows.append(window)
    result_windows_len = [len(x) for x in result_windows]
    result_windows_len_min = min(result_windows_len)
    result_windows = [x for x in result_windows if len(x) == result_windows_len_min]
    print(result_windows)

minimum_window_containing("PRWSOERIUSFK", "OSU")

