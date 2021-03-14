import itertools

string_maps = {
"1": "abc",
"2": "def",
"3": "ghi",
"4": "jkl",
"5": "mno",
"6": "pqrs",
"7": "tuv",
"8": "wxy",
"9": "z"
}

def letter_combinations(value):
    options = []
    value_str = str(value)
    for n in value_str:
        temp = []
        for c in string_maps[n]:
            temp.append(c)
        options.append(temp)
    results = [''.join(x) for x in list(itertools.product(*options))]
    print(results)

value = 47
letter_combinations(value)
value = 29
letter_combinations(value)


