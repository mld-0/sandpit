
def count_vowels(_str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count_vowels = {k: 0 for k in vowels}
    for c in _str:
        if c in vowels:
            count_vowels[c] += 1
    count_vowels = {k: v for k,v in sorted(count_vowels.items(), key=lambda x: x[1], reverse=True) if v > 0}
    print(count_vowels)

count_vowels('w3resource')
