
seperate_positive_negative = lambda x: [*[n for n in x if n >= 0], *[n for n in x if n < 0]]

values = [-1, 2, -3, 5, 7, 8, 9, -10]
print(seperate_positive_negative(values))

