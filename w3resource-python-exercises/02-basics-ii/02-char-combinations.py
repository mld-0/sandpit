import itertools

val_chars = ['a', 'e', 'i', 'o', 'u']

perms = list(itertools.permutations(val_chars))
perm_strs = [''.join(x) for x in perms]
print(perm_strs)

