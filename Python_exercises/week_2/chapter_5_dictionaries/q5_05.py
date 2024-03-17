def remove_key(dictionary, key):
    if key in dictionary:
        del dictionary[key]
    return dictionary

# Test:
print(remove_key({'a': 1, 'b': 2, 'c': 3}, 'b'))  