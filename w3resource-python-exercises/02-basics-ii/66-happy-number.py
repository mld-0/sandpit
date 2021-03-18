
def is_happy_number(n):
    seen = set()
    while (n > 1) and n not in seen:
        seen.add(n)
        n_str = str(n)
        n = sum([int(x) ** 2 for x in n_str])
    print(n==1)

is_happy_number(7)
is_happy_number(932)
is_happy_number(6)
