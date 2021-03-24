
def remove_words_containing_str(values, substrs):
    result = [x for x in values if not any([S in x for S in substrs])]
    print(result)

values = ['Red color', 'Orange#', 'Green', 'Orange @', 'White']
substrs = ['#', 'color', '@']

remove_words_containing_str(values, substrs)


