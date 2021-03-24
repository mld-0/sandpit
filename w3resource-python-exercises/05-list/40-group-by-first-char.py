import itertools

def group_by_first_char(word_list):
    word_list_sorted = sorted(word_list)
    results = []
    for c, words in itertools.groupby(word_list_sorted, lambda x: x[0]):
        loop_list = [c, [word for word in words]]
        results.append(loop_list)
    #   or
    results = [[c, [word for word in words]] for c, words in itertools.groupby(word_list_sorted, lambda x: x[0])]
    print(results)

word_list = ['be','have','do','say','get','make','go','know','take','see','come','think', 'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']
group_by_first_char(word_list)
