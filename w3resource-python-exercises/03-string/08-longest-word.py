
def longest_word(values):
    values_len = [len(x) for x in values]
    longest_index = values_len.index(max(values_len))
    print(values[longest_index])
    print(values_len[longest_index])

longest_word(["PHP", "Exercises", "Backend"])

