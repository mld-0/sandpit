
def remove_first_n_even(values, n):
    result = []
    removed_count = 0
    for x in values:
        if x % 2 != 0 or removed_count >= n:
            result.append(x)
        else:
            removed_count += 1
    print(result)
            
        

values = [3,10,4,7,5,7,8,3,3,4,5,9,3,4,9,8,5]
remove_first_n_even(values, 4)

values = [3, 10, 4, 7, 5, 7, 8, 3, 3, 4, 5, 9, 3, 4, 9, 8, 5]
remove_first_n_even(values, 4)

