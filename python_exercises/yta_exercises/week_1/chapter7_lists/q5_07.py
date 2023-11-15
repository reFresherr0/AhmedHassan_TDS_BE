def remove_duplicates(list):
    # A function that removes duplicates from a list while preserving the order of the original list.
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Test
print('Original list:', [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9])
print('Unique list is:', remove_duplicates([1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9])) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
