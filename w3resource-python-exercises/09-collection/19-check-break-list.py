import collections 

def check_break_list(nums, n):
    coll_data = collections.Counter(nums)
    result = None
    results = []
    for x in sorted(coll_data.keys()):  # x for each digit in nums
        if result is not None and len(result) > 1:
            results.append(result)
        result = [x]
        for index in range(1, n):  # next index-th digit for [1, n)
            _previous = coll_data[x+index]
            coll_data[x+index] -= coll_data[x]
            if _previous != coll_data[x+index]:
                result.append(x+index)
            if coll_data[x+index] < 0:
                return False
    print(results)
    return True

#nums = [1,2,3,4,5,6,7,8]
nums = [2,1,3,4,5,7,8,6]
n = 4
print(check_break_list(nums, n))

nums = [4,3,2,1,5,9,8,7,6]
n = 3
print(check_break_list(nums, n))
