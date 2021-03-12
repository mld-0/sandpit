n = 5
nums_as_str = [str(n), str(n) * 2, str(n) * 3]  # repeat string '*'
nums_as_int = [ int(x) for x in nums_as_str ]
nums_sum = sum(nums_as_int)
print(n)
print(nums_sum)
