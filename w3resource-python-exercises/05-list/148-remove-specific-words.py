
def remove_specific_words(values, _remove):
    result = [x for x in values if not x in _remove]
    print(result)

values = ['red', 'green', 'blue', 'white', 'black', 'orange']
_remove = ['white', 'orange']

remove_specific_words(values, _remove)
