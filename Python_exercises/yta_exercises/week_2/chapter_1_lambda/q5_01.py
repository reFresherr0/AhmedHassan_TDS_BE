from functools import reduce
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
max_num = reduce(lambda x, y: x if x > y else y, list)
print(max_num)
