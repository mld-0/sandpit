def filter_positive(nums):
    new_nums = [x for x in nums if x <= 0]
    nums[:] = new_nums[:]

nums = [34, 1, 0, -23]
print(nums)
filter_positive(nums)
print(nums)

