
def remove_duplicate_words(values):
    result = []
    for word in values:
        if not word in result:
            result.append(word)
    print(result)

values = ['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']
remove_duplicate_words(values)
