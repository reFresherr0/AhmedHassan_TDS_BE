from functools import reduce
nums = [1, 2, 3, 4, 5]
average = reduce(lambda x, y: x + y, nums) / len(nums)
print(average)