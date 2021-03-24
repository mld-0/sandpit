import random

def shuffle_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)
    
def scrable_letters_in_list(values):
    result = [shuffle_word(i) for i in values]
    print(result)

values = ['Python', 'list', 'exercises', 'practice', 'solution']
scrable_letters_in_list(values)
