
def extract_strings_of_length(values, n):
    result = [x for x in values if len(x) == n]
    print(result)


values = ['Python', 'list', 'exercises', 'practice', 'solution']
extract_strings_of_length(values, 8)
