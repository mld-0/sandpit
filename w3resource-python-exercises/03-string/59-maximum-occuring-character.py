from collections import Counter

def maximum_occuring_character(_str):
    unique_characters = set(_str[:])
    characters_count = Counter(_str[:])
    max_occur_char = list(sorted(characters_count.items(), key=lambda x: x[1], reverse=True))[0][0]
    print(max_occur_char)

maximum_occuring_character("Python: Get file creation and modification date/times")
maximum_occuring_character("abcdefghijkb")





