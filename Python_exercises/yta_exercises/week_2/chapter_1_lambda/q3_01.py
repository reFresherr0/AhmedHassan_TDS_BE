
tuples_list = [(1, 4), (2, 3), (3, 2), (4, 1)]
sorted_list = sorted(tuples_list, key=lambda x: x[1]) # sort by second element in tuple
print(sorted_list)
