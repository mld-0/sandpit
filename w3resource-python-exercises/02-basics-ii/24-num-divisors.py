def divisors_count(num):
    divisors = []
    for n in range(1, num):
        if num % n == 0:
            divisors.append(n)
    print(1+len(divisors), end="")
    print("\t", end="")
    if (1+len(divisors)) % 2 == 0:
        print("Even")
    else:
        print("Odd")

values = [15, 12, 9, 6, 3]
for value in values:
    divisors_count(value)
    
        
