def sort_dictionary(dictionary, by_key=True):
    if by_key:
        sorted_items = sorted(dictionary.items(), key=lambda x: x[0])
    else:
        sorted_items = sorted(dictionary.items(), key=lambda x: x[1])
    sorted_dict = dict(sorted_items)
    return sorted_dict

# Test:
print(sort_dictionary({'a': 1, 'b': 2, 'c': 3}, by_key=False))