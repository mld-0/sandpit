import re

#   LINK: https://diveintopython3.net/advanced-iterators.html

#   Explaining methods/techniques used in solver.py

#   the re.findall() function only returned three matches. Specifically, it returned the first, the third, and the fifth. Why is that? Because it doesn’t return overlapping matches. The first match overlaps with the second, so the first is returned and the second is skipped. Then the third overlaps with the fourth, so the third is returned and the fourth is skipped. Finally, the fifth is returned. Three matches, not five.
result = re.findall(' s.*? s', "The sixth sick sheikh's sixth sheep's sick.")
print(result)

#   Given a list of several strings, the set() function will return a set of unique strings from the list. This makes sense if you think of it like a for loop. Take the first item from the list, put it in the set. Second. Third. Fourth. Fifth — wait, that’s in the set already, so it only gets listed once, because Python sets don’t allow duplicates. Sixth. Seventh — again, a duplicate, so it only gets listed once. The end result? All the unique items in the original list, without any duplicates. The original list doesn’t even need to be sorted first.
a_list = ['The', 'sixth', 'sick', "sheik's", 'sixth', "sheep's", 'sick']
result = set(a_list)
print(result)


#   The same technique works with strings, since a string is just a sequence of characters.
a_string = 'EAST IS EAST'
result = set(a_string)
print(result)

#       Given a list of strings, ''.join(a_list) concatenates all the strings together into one.
words = ['SEND', 'MORE', 'MONEY']
result = ''.join(words)
print(result)

#   So, given a list of strings, this line of code returns all the unique characters across all the strings, with no duplicates.
words = ['SEND', 'MORE', 'MONEY']
result = set(''.join(words))
print(result)
print()

unique_characters = {'E', 'D', 'M', 'O', 'N', 'S', 'R', 'Y'}
#   A generator expression is like an anonymous function that yields values. The expression itself looks like a list comprehension, but it’s wrapped in parentheses instead of square brackets.
gen = (ord(c) for c in unique_characters)
#    The generator expression returns… an iterator.
print(gen)
print(next(gen))
print(next(gen))
result = tuple(ord(c) for c in unique_characters)
print(result)
print()

#   another way to accomplish the same thing, using a generator function
def ord_map(a_string):
    for c in a_string:
        yield ord(c)

gen = ord_map(unique_characters)
print(gen)
print(next(gen))
print(next(gen))
result = tuple(ord(c) for c in unique_characters)
print(result)
print()

import itertools

#   All possible permutations of [1,2,3] of length 2
perms = itertools.permutations([1, 2, 3], 2)
print(list(perms))
#   The itertools.product() function returns an iterator containing the Cartesian product of two sequences.
print(list(itertools.product('ABC', '123')))
#   The itertools.combinations() function returns an iterator containing all the possible combinations of the given sequence of the given length. This is like the itertools.permutations() function, except combinations don’t include items that are duplicates of other items in a different order. So itertools.permutations('ABC', 2) will return both ('A', 'B') and ('B', 'A') (among others), but itertools.combinations('ABC', 2) will not return ('B', 'A') because it is a duplicate of ('A', 'B') in a different order.
print(list(itertools.combinations('ABC', 2)))
print()

names = ['Dora', 'Ethan', 'Wesley', 'John', 'Anne', 'Mike', 'Chris', 'Sarah', 'Alex', 'Lizzie']
#   sorted alphabetically
print(sorted(names))
#   sort by length - stable sort, preserves order of items of same length
print(sorted(names, key=len))

#   The itertools.groupby() function only works if the input sequence is already sorted by the grouping function. In the example above, you grouped a list of names by the len() function. That only worked because the input list was already sorted by length.
names = sorted(names, key=len)
groups = itertools.groupby(names, len)
for name_length, name_iter in groups:
    print('Names with {0:d} letters:'.format(name_length))
    for name in name_iter:
        print(name)
print()

print(list(range(0, 3)))
print(list(range(10, 13)))
#   The itertools.chain() function takes two iterators and returns an iterator that contains all the items from the first iterator, followed by all the items from the second iterator. (Actually, it can take any number of iterators, and it chains them all in the order they were passed to the function.)
print(list(itertools.chain(range(0, 3), range(10, 13))))
#   The zip() function does something prosaic that turns out to be extremely useful: it takes any number of sequences and returns an iterator which returns tuples of the first items of each sequence, then the second items of each, then the third, and so on.
print(list(zip(range(0, 3), range(10, 13))))
#   The zip() function stops at the end of the shortest sequence. range(10, 14) has 4 items (10, 11, 12, and 13), but range(0, 3) only has 3, so the zip() function returns an iterator of 3 items.
print(list(zip(range(0, 3), range(10, 14))))
#   On the other hand, the itertools.zip_longest() function stops at the end of the longest sequence, inserting None values for items past the end of the shorter sequences.
print(list(itertools.zip_longest(range(0, 3), range(10, 14))))
print()

characters = ('S', 'M', 'E', 'D', 'O', 'N', 'R', 'Y')
guess = ('1', '2', '0', '3', '4', '5', '6', '7')
#   Given a list of letters and a list of digits (each represented here as 1-character strings), the zip function will create a pairing of letters and digits, in order.
print(tuple(zip(characters, guess)))
print(dict(zip(characters, guess)))
print()

#   Using a generator expression, we quickly compute the byte values for each character in a string. characters is an example of the value of sorted_characters in the alphametics.solve() function.
characters = tuple(ord(c) for c in 'SMEDONRY')
print(characters)
#   Using another generator expression, we quickly compute the byte values for each digit in this string. The result, guess, is of the form returned by the itertools.permutations() function in the alphametics.solve() function.
guess = tuple(ord(c) for c in '91570682')
print(guess)
#   This translation table is generated by zipping characters and guess together and building a dictionary from the resulting sequence of pairs. This is exactly what the alphametics.solve() function does inside the for loop.
translation_table = dict(zip(characters, guess))
print(translation_table)
#   Finally, we pass this translation table to the translate() method of the original puzzle string. This converts each letter in the string to the corresponding digit (based on the letters in characters and the digits in guess). The result is a valid Python expression, as a string.
result = 'SEND + MORE == MONEY'.translate(translation_table)
print(result)
#   And evaulate it using eval(). The pitfalls of which (are discussed elsewhere)
print(eval(result))



