from collections import Counter

def count_word_occurences(values):
    result_counter = Counter(values)
    print(result_counter.most_common(4))

words = [ 'red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes', 'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange', 'white', "black", 'pink', 'green', 'green', 'pink', 'green', 'pink', 'white', 'orange', "orange", 'red' ]
count_word_occurences(words)
