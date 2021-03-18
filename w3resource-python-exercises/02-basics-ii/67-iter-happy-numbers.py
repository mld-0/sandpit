
def is_happy_number(n):
    seen = set()
    while (n > 1) and n not in seen:
        seen.add(n)
        n_str = str(n)
        n = sum([int(x) ** 2 for x in n_str])
    return n == 1

def iter_happy_numbers(count_max):
    happy_numbers = []
    n = 0
    while (len(happy_numbers) < count_max):
        n += 1
        if is_happy_number(n):
            happy_numbers.append(n)
    print(happy_numbers)
        
iter_happy_numbers(10)
    
