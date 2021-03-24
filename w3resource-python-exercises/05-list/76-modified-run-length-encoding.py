import itertools

def modified_run_length_encoding(values):
    if isinstance(values, str):
        values = [x for x in values]
    result = [[g_len, k] if (g_len := len(list(g))) > 1 else k for k, g in itertools.groupby(values)]
    print(result)

values = [1, 1, 2, 3, 4, 4, 5, 1]
modified_run_length_encoding(values)

values = 'aabcddddadnss'
modified_run_length_encoding(values)
