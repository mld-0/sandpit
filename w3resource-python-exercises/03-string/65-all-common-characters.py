from collections import Counter

def all_common_characters(str1, str2):
    str1_chars = set(str1)
    str2_chars = set(str2)

    str1_chars_count = Counter(str1)
    str2_chars_count = Counter(str2)

    common_chars = str1_chars & str2_chars
    common_chars_count = {x: str1_chars_count[x] + str2_chars_count[x] for x in common_chars}

    if len(common_chars) == 0:
        print(None)
        return
    for k, v in sorted(common_chars_count.items(), key=lambda x: x[1], reverse=True):
        print(k)

str1 = 'Python'
str2 = 'PHP'
all_common_characters(str1, str2)

str1 = 'Java'
str2 = 'PHP'
all_common_characters(str1, str2)

