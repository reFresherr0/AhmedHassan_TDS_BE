def filter_dict(dictionary, condition_func):
    filtered_dict = {}
    for key, value in dictionary.items():
        if condition_func(key, value):
            filtered_dict[key] = value
    return filtered_dict

# Test:
print(filter_dict({'a': 1, 'b': 2, 'c': 3}, lambda key, value: value > 1))