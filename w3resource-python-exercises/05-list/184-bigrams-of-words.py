
def bigrams_of_words(values):
    result = []
    for L in values:
        words = L.split(' ')
        for i in range(len(words)-1):
            loop_result = (words[i], words[i+1])
            result.append(loop_result)
    #   or
    result = [(words[i], words[i+1]) for L in values for i in range(len(L.split(' '))-1)]
    print(result)
            
values = ['Sum all the items in a list', 'Find the second smallest number in a list']
bigrams_of_words(values)
