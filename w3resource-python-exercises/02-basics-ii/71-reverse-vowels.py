import re

def reverse_vowels(_str):
    finditer_vowels = re.finditer('[AEIOUaeiou]', _str)
    _vowel_values, _vowel_positions = zip(*[[x.group(), x.start()] for x in finditer_vowels])
    result = str(_str)
    for loop_vowel, loop_position in zip(_vowel_values, reversed(_vowel_positions)):
        result = result[:loop_position] + loop_vowel + result[loop_position+1:]
    print(result)

reverse_vowels("w3resource")
reverse_vowels("Python")
reverse_vowels("Perl")
reverse_vowels("USA")

