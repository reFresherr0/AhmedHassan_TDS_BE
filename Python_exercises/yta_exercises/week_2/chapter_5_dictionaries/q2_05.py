def search_key(dictionary, key, default_value = None):
    return dictionary.get(key, default_value)

# Test:
print(search_key({'a': 1, 'b': 2}, 'a'))
